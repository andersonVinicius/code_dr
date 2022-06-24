%Para 30 x 30 ------------------------------------------------------
% Create figure
figure1 = figure;
axes1 = axes('Parent',figure1);
title('');
% colormap(Parula);
hold(axes1,'on');
path_uav = [15, 45, 74, 103, 132, 162, 193, 222, 253, 284, 313, 343, 373, 402, 432, 462, 491, 522, 553, 584, 615, 646, 675, 704, 735, 765, 795, 824, 855, 884]
path_uav_egreedy = [15, 45, 74, 103, 132, 162, 193, 222, 253, 284, 313, 343, 373, 402, 432, 462, 492, 523, 554, 585, 615, 646, 675, 704, 735, 765, 795, 824, 855, 884]

path_uav_sarsa = [15, 45, 75, 105, 135, 165, 195, 224, 254, 284, 315, 345, 375, 405, 404, 403, 402, 433, 432, 463, 462, 493, 523, 554, 585, 615, 646, 675, 704, 735, 765, 794, 824, 854, 885] 

wind_amb_aux = windambiente
wind_amb_aux(path_uav) = -1

wind_matrix = reshape(windambiente,30,30)
wind_matrix_aux = reshape(wind_amb_aux,30,30)

[l, c]=find(wind_matrix_aux==-1)



% A(3:5,15)= 2
% A(24:25, 23:28) = 2
% A(5:6,5:6) = 2
% A(10:11,10:11) = 2
% % A(15:16, 22:24) = 2
% A(11:19, 15) = 2
% A(11:15, 14) = 2
% A(15,7:8) = 2
% A(25,5:9) = 2
% A(21:25,9) = 2
% A(6, 21:25) = 2
% A(6:9, 21) = 2
% A(17:20, 21) = 2
% A(20, 21:24) = 2
%iniwind_matrix 
% pcolor(A)
h=surface(wind_matrix ,'Parent',axes1,'AlignVertexCenters','on',...
    'CData',wind_matrix );
shading interp;
box(axes1,'on');
hold on 
z_max = max(max(get(h,'Zdata')))
line(l,c,z_max*ones(1,length(path_uav)),'DisplayName','simple Q-learning','Marker','^','LineWidth',2,'LineStyle',':','Color',[0 1 0])

hold on

wind_amb_aux = windambiente
wind_amb_aux(path_uav_egreedy) = -2
wind_matrix_aux = reshape(wind_amb_aux,30,30)
[l_egreedy, c_egreedy]=find(wind_matrix_aux==-2)
line(l_egreedy,c_egreedy,z_max*ones(1,length(path_uav_q_egreed)),'DisplayName','Q-learning egreedy','LineStyle','--','Marker','hexagram','LineWidth',2,'Color',[0.635294139385223 0.0784313753247261 0.184313729405403])
% view(axes1,[90.4000000000001 -90]);

hold on

wind_amb_aux = windambiente
wind_amb_aux(path_uav_sarsa) = -3
wind_matrix_aux = reshape(wind_amb_aux,30,30)
[l_sarsa, c_sarsa]=find(wind_matrix_aux==-3)
line(l_sarsa,c_sarsa,z_max*ones(1,length(path_uav_sarsa)),'DisplayName','Sarsa','Marker','hexagram','LineWidth',2,'Color',[0.952941179275513 0.87058824300766 0.733333349227905])


% Create colorbar
colorbar('peer',axes1);
view(axes1,[90.4 90]);

% Create textarrow
annotation(figure1,'textarrow',[0.94321206743567 0.903283052351376],...
    [0.542443917851501 0.518167456556082],'String',{'TARGET'},...
    'FontWeight','bold');

% Create textarrow
annotation(figure1,'textarrow',[0.11002661934339 0.152617568766637],...
    [0.552922590837283 0.521327014218009],'String',{'START'},...
    'FontWeight','bold');
% 
% x = peaks;
% h = surface(x);
% hold on
%    z_max = max(max(get(h,'Zdata')))
% line(1:50,1:50,z_max*ones(1,50))