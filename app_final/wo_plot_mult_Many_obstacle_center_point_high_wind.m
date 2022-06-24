% 
%Para 30 x 30 ------------------------------------------------------

subplot(7,2,[1 2 3 4]);
title('UAV path obstacle [Multi obstacle]');
A = repmat([repmat([0],1,30);repmat([0],1, 30)],15,1)
% A(13:15,15) = 1

A(15,1) = 1
A(15,29) = 1
for i= 9:2:22
    for j=9:2:22
    A(i,j)= 2
   
    end     
end  

% for i= 8:2:23
%     for j=8:2:23
%     A(i,j)= 2
%    
%     end     
% end  
%set wind turbulance 

% for i= 15:2:27
%     for j=3:2:27
%     A(i,j)= 2
%     end     
% end    
%ini
% pcolor(A)
h=surface(A);
% box(axes1,'on');
% view(axes1,[90.4000000000001 -90]);

grid_vet = A(:)'
grids_ids = find(grid_vet==2)
vet_to_py = ' '
for i=1:length(grids_ids)
    vet_to_py=strcat(num2str(grids_ids(i)),',', vet_to_py) 
end    
path_uav = [15, 45, 74, 105, 106, 137, 168, 198, 227, 258, 289, 320, 349, 380, 411, 440, 469, 498, 529, 560, 589, 618, 647, 678, 708, 737, 766, 795, 824, 855, 884, 885]
path_uav_egreedy =  [15, 45, 74, 105, 106, 137, 168, 198, 227, 258, 289, 320, 349, 380, 411, 440, 471, 502, 533, 562, 591, 620, 649, 678, 708, 737, 766, 795, 824, 855, 884]
path_uav_sarsa = [15, 45, 75, 106, 136, 166, 195, 225, 256, 285, 314, 345, 376, 405, 435, 434, 465, 495, 494]
    
% path_uav =  [15, 45, 75, 105, 136, 165, 195, 225, 254, 285, 314, 343, 372, 401, 430, 459, 488, 519, 548, 579, 610, 641, 671, 702, 733, 764, 795, 825, 855, 885]
grid_vet(path_uav) = 4
A = reshape(grid_vet,30,30)


hold on 
z_max = max(max(get(h,'Zdata')))
[l, c]=find(A==4)
line(c,l,ones(1,length(unique(path_uav))),'DisplayName','Simple Q-learning','LineStyle','--','Marker','hexagram','LineWidth',2,'Color',[0.635294139385223 0.0784313753247261 0.184313729405403])

hold on
A = repmat([repmat([0],1,30);repmat([0],1, 30)],15,1)
grid_vet = A(:)'
% path_uav_q_egreed = [15, 45, 74, 105, 136, 165, 194, 225, 254, 283, 312, 341, 370, 399, 428, 459, 488, 518, 547, 578, 608, 639, 670, 701, 732, 763, 794, 825, 855, 885] 
grid_vet(path_uav_egreedy) = 5

A = reshape(grid_vet,30,30)

[l_egreedy, c_egreedy]=find(A==5)
line(c_egreedy,l_egreedy,ones(1,length(unique(path_uav_egreedy))),'DisplayName','Q-learning egreedy','LineStyle',':','Marker','hexagram','LineWidth',2,'Color',[0 1 0])

hold on

A = repmat([repmat([0],1,30);repmat([0],1, 30)],15,1)
grid_vet = A(:)'
% path_uav_sarsa = [15, 45, 74, 104, 135, 164, 193, 224, 254, 284, 314, 345, 375, 374, 405, 435, 434, 464, 494, 524, 554, 585, 614, 645, 675, 704, 734, 765, 795, 826, 855, 885]
grid_vet(path_uav_sarsa) = 6

A = reshape(grid_vet,30,30)

[l_sarsa, c_sarsa]=find(A==6)
line(c_sarsa,l_sarsa,ones(1,length(unique(path_uav_sarsa))),'DisplayName','Sarsa','LineStyle',':','Marker','hexagram','LineWidth',2,'Color',[0.952941179275513 0.87058824300766 0.733333349227905])

view([126.4 61.2]);
legend1 = legend('show');
set(legend1,...
    'Position',[0.218524362096313 0.562391915186002 0.654269960957782 0.0210176986205367],...
    'Orientation','horizontal');




%q_learning_simple ---

subplot(7,2,5);
A = repmat([repmat([0],1,30);repmat([0],1, 30)],15,1)
A(15,1) = 1
A(15,29) = 1

for i= 9:2:22
    for j=9:2:22
    A(i,j)= 2
    end     
end 


grid_vet = A(:)'
grid_vet(path_uav) = 4
A = reshape(grid_vet,30,30)
% Create axes



title('Path planing Simple Q-learning WO');

surface(A);
% view(axes1b,[90.4000000000001 -90]);


%-------------------------------------------------------------
%q-learning egreedy
subplot(7,2,6);
A = repmat([repmat([0],1,30);repmat([0],1, 30)],15,1)
A(15,1) = 1
A(15,29) = 1

for i= 9:2:22
    for j=9:2:22
    A(i,j)= 2
    end     
end 

grid_vet = A(:)'
% path_uav = path_uav_egreedy
grid_vet(path_uav_egreedy) = 5
A = reshape(grid_vet,30,30)
% Create axes

title('Path planing Q-learning egreedy WO');

surface(A);
% view(axes1c,[90.4000000000001 -90]);

%------------------------------------------------------------
%SARSA

%q-learning egreedy

subplot(7,2, 7);
A = repmat([repmat([0],1,30);repmat([0],1, 30)],15,1)
A(15,1) = 1
A(15,29) = 1

for i= 9:2:22
    for j=9:2:22
    A(i,j)= 2
    end     
end 

grid_vet = A(:)'
% path_uav = path_uav_sarsa
grid_vet(path_uav_sarsa) = 6
A = reshape(grid_vet,30,30)

% Create title
title('Path planing Sarsa WO');

surface(A);
% view(axes1d,[90.4000000000001 -90]);

%cenario original 
subplot(7,2,8);

A = repmat([repmat([0],1,30);repmat([0],1, 30)],15,1)
A(15,1) = 1
A(15,29) = 1
for i= 9:2:22
    for j=9:2:22
    A(i,j)= 2
    end     
end 

% A(20, 21:24) = 2
A(30,30) = 5

% Create title
title('Scenario');

title('Obstacle scenario');
surface(A);


subplot(7,2,[9 10 11 12 13 14]);
% path_uav = [15, 45, 74, 105, 106, 137, 168, 198, 227, 258, 289, 320, 349, 380, 411, 440, 469, 498, 529, 560, 589, 618, 647, 678, 708, 737, 766, 795, 824, 855, 884, 885]
% path_uav_egreedy =  [15, 45, 74, 105, 106, 137, 168, 198, 227, 258, 289, 320, 349, 380, 411, 440, 471, 502, 533, 562, 591, 620, 649, 678, 708, 737, 766, 795, 824, 855, 884]
% path_uav_sarsa = [15, 45, 75, 106, 136, 166, 195, 225, 256, 285, 314, 345, 376, 405, 435, 434, 465, 495, 494]
title('UAV path analyze wind speed [Mult obstacle]');
% colormap(Parula);
% hold(axes1,'on');


wind_amb_aux = windambiente
wind_amb_aux(path_uav) = -1

wind_matrix = reshape(windambiente,30,30)
wind_matrix_aux = reshape(wind_amb_aux,30,30)

[l, c]=find(wind_matrix_aux==-1)



h=surface(wind_matrix);
shading interp;
% box(axes1,'on');

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
% colorbar('peer');
% view([90.4 90]);

% % Create textarrow
% annotation(figure1,'textarrow',[0.11002661934339 0.152617568766637],...
%     [0.552922590837283 0.521327014218009],'String',{'START'},...
%     'FontWeight','bold');
% 
% % Create textarrow
% annotation(figure1,'textarrow',[0.91289592760181 0.826923076923077],...
%     [0.539267015706806 0.520069808027923],'String',{'TARGET'},...
%     'FontWeight','bold');

view([1.36779476633819e-13 90]);
% Create legend
legend1 = legend('show');
set(legend1,...
    'Position',[0.220701364002516 0.0257853422645501 0.552036189217104 0.0331588124833598],...
    'Orientation','horizontal');

