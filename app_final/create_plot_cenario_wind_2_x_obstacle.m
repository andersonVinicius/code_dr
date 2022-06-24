%Para 30 x 30 ------------------------------------------------------
% Create figure
figure1 = figure;
axes1 = axes('Parent',figure1);
title('UAV path analyze wind speed [2 x obstacle]');
% colormap(Parula);
hold(axes1,'on');
path_uav = [15, 45, 75, 106, 137, 168, 198, 228, 257, 286, 315, 344, 373, 402, 432, 462, 492, 523, 554, 585, 615, 646, 675, 704, 735, 765, 795, 824, 855, 885]
path_uav_egreedy =  [15, 45, 75, 106, 137, 168, 198, 228, 259, 290, 320, 349, 379, 408, 438, 468, 498, 528, 557, 586, 615, 646, 675, 704, 735, 765, 795, 824, 855, 885] 

path_uav_sarsa = [15, 46, 76, 105, 136, 165, 195, 194, 193, 192, 191, 222, 221, 251, 282, 313, 344, 373, 404, 403, 402, 433, 432, 463, 462, 493, 524, 554, 585, 616, 645, 676, 706, 735, 765, 795, 826, 855, 885]

wind_amb_aux = windambiente
wind_amb_aux(path_uav) = -1

wind_matrix = reshape(windambiente,30,30)
wind_matrix_aux = reshape(wind_amb_aux,30,30)

[l, c]=find(wind_matrix_aux==-1)



h=surface(wind_matrix ,'Parent',axes1,'AlignVertexCenters','on',...
    'CData',wind_matrix );
shading interp;
box(axes1,'on');
hold on 
z_max = max(max(get(h,'Zdata')))
line(c,l,z_max*ones(1,length(path_uav)),'DisplayName','simple Q-learning','Marker','^','LineWidth',2,'LineStyle',':','Color',[0 1 0])

hold on

wind_amb_aux = windambiente
wind_amb_aux(path_uav_egreedy) = -2
wind_matrix_aux = reshape(wind_amb_aux,30,30)
[l_egreedy, c_egreedy]=find(wind_matrix_aux==-2)
line(c_egreedy,l_egreedy, z_max*ones(1,length(path_uav_egreedy)),'DisplayName','Q-learning egreedy','LineStyle','--','Marker','hexagram','LineWidth',2,'Color',[0.635294139385223 0.0784313753247261 0.184313729405403])
% view(axes1,[90.4000000000001 -90]);

hold on

wind_amb_aux = windambiente
wind_amb_aux(path_uav_sarsa) = -3
wind_matrix_aux = reshape(wind_amb_aux,30,30)
[l_sarsa, c_sarsa]=find(wind_matrix_aux==-3)
line(c_sarsa,l_sarsa,z_max*ones(1,length(path_uav_sarsa)),'DisplayName','Sarsa','Marker','hexagram','LineWidth',2,'Color',[0.952941179275513 0.87058824300766 0.733333349227905])


% Create colorbar
colorbar('peer',axes1);
view(axes1,[90.4 90]);

% Create textarrow
annotation(figure1,'textarrow',[0.11002661934339 0.152617568766637],...
    [0.552922590837283 0.521327014218009],'String',{'START'},...
    'FontWeight','bold');

% Create textarrow
annotation(figure1,'textarrow',[0.91289592760181 0.826923076923077],...
    [0.539267015706806 0.520069808027923],'String',{'TARGET'},...
    'FontWeight','bold');

view([1.36779476633819e-13 90]);
% Create legend
legend1 = legend('show');
set(legend1,...
    'Position',[0.220701364002516 0.0257853422645501 0.552036189217104 0.0331588124833598],...
    'Orientation','horizontal');
% 
% x = peaks;
% h = surface(x);
% hold on
%    z_max = max(max(get(h,'Zdata')))
% line(1:50,1:50,z_max*ones(1,50))