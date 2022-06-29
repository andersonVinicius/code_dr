load('center_points_max_wind_speed.mat')
path_uav = [15, 45, 74, 105, 106, 137, 168, 198, 227, 258, 289, 320, 349, 380, 411, 440, 469, 498, 529, 560, 589, 618, 647, 678, 708, 737, 766, 795, 824, 855, 884, 885]
path_uav_egreedy =  [15, 45, 74, 105, 106, 137, 168, 198, 227, 258, 289, 320, 349, 380, 411, 440, 471, 502, 533, 562, 591, 620, 649, 678, 708, 737, 766, 795, 824, 855, 884]
path_uav_sarsa = [15, 45, 75, 106, 136, 166, 195, 225, 256, 285, 314, 345, 376, 405, 435, 434, 465, 495, 494]

% Create figure
figure1 = figure;
figure1.Position = [1000 2600 900 2600]
% Create axes
% Create axes
axes1 = axes('Parent',figure1,...
    'Position',[0.13 0.716398809523809 0.775 0.208601190476191]);
hold(axes1,'on');

%Para 30 x 30 ------------------------------------------------------

subplot1 = subplot(9,2,[1 2 3 4],'Parent',figure1);
hold(subplot1,'on');
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
h=surface(A,'Parent',subplot1,'DisplayName','');
% box(axes1,'on');
% view(axes1,[90.4000000000001 -90]);

grid_vet = A(:)'
grids_ids = find(grid_vet==2)
vet_to_py = ' '
for i=1:length(grids_ids)
    vet_to_py=strcat(num2str(grids_ids(i)),',', vet_to_py) 
end    

    
% path_uav =  [15, 45, 75, 105, 136, 165, 195, 225, 254, 285, 314, 343, 372, 401, 430, 459, 488, 519, 548, 579, 610, 641, 671, 702, 733, 764, 795, 825, 855, 885]
grid_vet(path_uav) = 4
A = reshape(grid_vet,30,30)


hold on 
z_max = max(max(get(h,'Zdata')))
[l, c]=find(A==4)
line(c,l,ones(1,length(unique(path_uav))),'Parent',subplot1,'DisplayName','Simple Q-learning','LineStyle','--','Marker','hexagram','LineWidth',2,'Color',[0.635294139385223 0.0784313753247261 0.184313729405403])

hold on
A = repmat([repmat([0],1,30);repmat([0],1, 30)],15,1)
grid_vet = A(:)'
% path_uav_q_egreed = [15, 45, 74, 105, 136, 165, 194, 225, 254, 283, 312, 341, 370, 399, 428, 459, 488, 518, 547, 578, 608, 639, 670, 701, 732, 763, 794, 825, 855, 885] 
grid_vet(path_uav_egreedy) = 5

A = reshape(grid_vet,30,30)

[l_egreedy, c_egreedy]=find(A==5)
line(c_egreedy,l_egreedy,ones(1,length(unique(path_uav_egreedy))),'Parent',subplot1,'DisplayName','Q-learning egreedy','LineStyle',':','Marker','hexagram','LineWidth',2,'Color',[0 1 0])

hold on

A = repmat([repmat([0],1,30);repmat([0],1, 30)],15,1)
grid_vet = A(:)'
% path_uav_sarsa = [15, 45, 74, 104, 135, 164, 193, 224, 254, 284, 314, 345, 375, 374, 405, 435, 434, 464, 494, 524, 554, 585, 614, 645, 675, 704, 734, 765, 795, 826, 855, 885]
grid_vet(path_uav_sarsa) = 6

A = reshape(grid_vet,30,30)

[l_sarsa, c_sarsa]=find(A==6)
line(c_sarsa,l_sarsa,ones(1,length(unique(path_uav_sarsa))),'Parent',subplot1,'DisplayName','Sarsa','LineStyle',':','Marker','hexagram','LineWidth',2,'Color',[0.952941179275513 0.87058824300766 0.733333349227905])

view([0.4 90]);
% Create legend
% legend1 = legend('show');
% set(legend1,...
%     'Position',[0.567703398700966 0.484723676758788 0.349895536562202 0.0584229374444613],...
%     'FontSize',12);



%q_learning_simple ---

subplot1a = subplot(9,2,[5  7],'Parent',figure1);
hold(subplot1a,'on');
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

surface(A,'Parent',subplot1a);
% view(axes1b,[90.4000000000001 -90]);


%-------------------------------------------------------------
%q-learning egreedy---------------------------------------------
subplot2 = subplot(9,2,[6 8],'Parent',figure1);
hold(subplot2,'on');
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

surface(A,'Parent',subplot2);
% view(axes1c,[90.4000000000001 -90]);

%------------------------------------------------------------
%SARSA---------------------------------------------------------
subplot3 = subplot(9,2,[9,11],'Parent',figure1);
hold(subplot3,'on');

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

surface(A,'Parent',subplot3);
% view(axes1d,[90.4000000000001 -90]);

% %cenario original -
% subplot(7,2,8);
% 
% A = repmat([repmat([0],1,30);repmat([0],1, 30)],15,1)
% A(15,1) = 1
% A(15,29) = 1
% for i= 9:2:22
%     for j=9:2:22
%     A(i,j)= 2
%     end     
% end 
% 
% % A(20, 21:24) = 2
% A(30,30) = 5
% 
% % Create title
% title('Scenario');
% 
% title('Obstacle scenario');
% surface(A);

% Create axes
% axes2 = axes('Parent',figure1,...
%     'Position',[0.126296296296296 0.11 0.778703703703704 0.30599387311928]);
% hold(axes2,'on');


sub4 = subplot(9,2,[13 14 15 16 17 18],'Parent',figure1);
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



h=surface(wind_matrix,'Parent',sub4);
shading interp;
% box(axes1,'on');

hold on 
z_max = max(max(get(h,'Zdata')))
line(c,l,z_max*ones(1,length(path_uav)),'Parent',sub4 ,'DisplayName','Simple Q-learning','LineStyle','--','Marker','hexagram','LineWidth',2,'Color',[0.635294139385223 0.0784313753247261 0.184313729405403])

hold on

wind_amb_aux = windambiente
wind_amb_aux(path_uav_egreedy) = -2
wind_matrix_aux = reshape(wind_amb_aux,30,30)
[l_egreedy, c_egreedy]=find(wind_matrix_aux==-2)
line(c_egreedy,l_egreedy, z_max*ones(1,length(path_uav_egreedy)),'Parent',sub4 ,'DisplayName','Q-learning egreedy','LineStyle',':','Marker','hexagram','LineWidth',2,'Color',[0 1 0])
% view(axes1,[90.4000000000001 -90]);

hold on

wind_amb_aux = windambiente
wind_amb_aux(path_uav_sarsa) = -3
wind_matrix_aux = reshape(wind_amb_aux,30,30)
[l_sarsa, c_sarsa]=find(wind_matrix_aux==-3)
line(c_sarsa,l_sarsa,z_max*ones(1,length(path_uav_sarsa)),'Parent',sub4 ,'DisplayName','Sarsa','Marker','hexagram','LineWidth',2,'Color',[0.952941179275513 0.87058824300766 0.733333349227905])

% colorbar('peer','Position',...
%     [0.126296296296296 0.0613378535687142 0.778703703703703 0.0193648316120883]);
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

view(axes2,[1.36779476633819e-13 90]);
% Create legend
% legend1 = legend('show');
% set(legend1,...
%     'Position',[0.220701364002516 0.0257853422645501 0.552036189217104 0.0331588124833598],...
%     'Orientation','horizontal');



% colorbar('peer',axes2,'southoutside','Position',...
%     [0.126296296296296 0.0613378535687142 0.778703703703703 0.0193648316120883]);
% % Create rectangle
% annotation(figure1,'rectangle',...
%     [0.628096901519637 0.532973552908928 0.0663475429248069 0.0206164574968998],...
%     'LineStyle','none',...
%     'FaceColor',[1 1 1]);
% % Create textbox
% annotation(figure1,'textbox',...
%     [0.460340659340659 0.0166493236212279 0.148450549450549 0.0260145681581687],...
%     'String',{'Wind Speed (m/s)'},...
%     'LineStyle','none',...
%     'FitBoxToText','off');
