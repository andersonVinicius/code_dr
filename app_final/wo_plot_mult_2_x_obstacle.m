% 
%Para 30 x 30 ------------------------------------------------------

subplot(5,2,[1 2 3 4]);
title('UAV path obstacle [2 x obstacle]');
A = repmat([repmat([0],1,30);repmat([0],1, 30)],15,1)
% A(13:15,15) = 1

A(15,1) = 1
A(15,29) = 1
%obst 1---------------------
A(13,14:16) = 2
A(14:16,14) = 2
A(17,14:16) = 2
A(14:16,16) = 2
% ---------------------------

%obst 2 ---------------------
A(12,7:8) = 3
A(13,7:8) = 3
A(14,7:8) = 3
A(15,7:8) = 3
A(16,7:8) = 3

%obst 3 --------------------
% A(14,19:20) = 2
% A(15,19:20) = 2
% A(16,19:20) = 2


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

    
path_uav = [15, 45, 75, 106, 137, 168, 198, 228, 257, 286, 315, 344, 373, 402, 432, 462, 492, 523, 554, 585, 615, 646, 675, 704, 735, 765, 795, 824, 855, 885]
grid_vet(path_uav) = 4
A = reshape(grid_vet,30,30)


hold on 
z_max = max(max(get(h,'Zdata')))
[l, c]=find(A==4)
line(c,l,ones(1,length(unique(path_uav))),'DisplayName','Simple Q-learning','LineStyle','--','Marker','hexagram','LineWidth',2,'Color',[0.635294139385223 0.0784313753247261 0.184313729405403])

hold on
A = repmat([repmat([0],1,30);repmat([0],1, 30)],15,1)
grid_vet = A(:)'
path_uav_q_egreed = [15, 45, 75, 106, 137, 168, 198, 228, 259, 290, 320, 349, 379, 408, 438, 468, 498, 528, 557, 586, 615, 646, 675, 704, 735, 765, 795, 824, 855, 885] 
grid_vet(path_uav_q_egreed) = 5

A = reshape(grid_vet,30,30)

[l_egreedy, c_egreedy]=find(A==5)
line(c_egreedy,l_egreedy,ones(1,length(unique(path_uav_q_egreed))),'DisplayName','Q-learning egreedy','LineStyle',':','Marker','hexagram','LineWidth',2,'Color',[0 1 0])

hold on

A = repmat([repmat([0],1,30);repmat([0],1, 30)],15,1)
grid_vet = A(:)'
path_uav_sarsa = [15, 46, 76, 105, 136, 165, 195, 194, 193, 192, 191, 222, 221, 251, 282, 313, 344, 373, 404, 403, 402, 433, 432, 463, 462, 493, 524, 554, 585, 616, 645, 676, 706, 735, 765, 795, 826, 855, 885]
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

subplot(4,2,5);
A = repmat([repmat([0],1,30);repmat([0],1, 30)],15,1)
A(15,1) = 1
A(15,29) = 1
%obst 1---------------------
A(13,14:16) = 2
A(14:16,14) = 2
A(17,14:16) = 2
A(14:16,16) = 2
% ---------------------------

%obst 2 ---------------------
A(14,7:8) = 2
A(15,7:8) = 2
A(16,7:8) = 2

%obst 3 --------------------
% A(14,19:20) = 2
% A(15,19:20) = 2
% A(16,19:20) = 2



grid_vet = A(:)'
grid_vet(path_uav) = 4
A = reshape(grid_vet,30,30)
% Create axes



title('Path planing Simple Q-learning WO');

surface(A);
% view(axes1b,[90.4000000000001 -90]);


%-------------------------------------------------------------
%q-learning egreedy
subplot(4,2,6);
A = repmat([repmat([0],1,30);repmat([0],1, 30)],15,1)
A(15,1) = 1
A(15,29) = 1
%obst 1---------------------
A(13,14:16) = 2
A(14:16,14) = 2
A(17,14:16) = 2
A(14:16,16) = 2
% ---------------------------

%obst 2 ---------------------
A(14,7:8) = 2
A(15,7:8) = 2
A(16,7:8) = 2

%obst 3 --------------------
% A(14,19:20) = 2
% A(15,19:20) = 2
% A(16,19:20) = 2


grid_vet = A(:)'
path_uav = path_uav_q_egreed
grid_vet(path_uav) = 5
A = reshape(grid_vet,30,30)
% Create axes

title('Path planing Q-learning egreedy WO');

surface(A);
% view(axes1c,[90.4000000000001 -90]);

%------------------------------------------------------------
%SARSA

%q-learning egreedy

subplot(4,2, 7);
A = repmat([repmat([0],1,30);repmat([0],1, 30)],15,1)
A(15,1) = 1
A(15,29) = 1
%obst 1---------------------
A(13,14:16) = 2
A(14:16,14) = 2
A(17,14:16) = 2
A(14:16,16) = 2
% ---------------------------

%obst 2 ---------------------
A(14,7:8) = 2
A(15,7:8) = 2
A(16,7:8) = 2

%obst 3 --------------------
% A(14,19:20) = 2
% A(15,19:20) = 2
% A(16,19:20) = 2


grid_vet = A(:)'
path_uav = path_uav_sarsa
grid_vet(path_uav) = 6
A = reshape(grid_vet,30,30)

% Create title
title('Path planing Sarsa WO');

surface(A);
% view(axes1d,[90.4000000000001 -90]);

%cenario original 
subplot(4,2,8);

A = repmat([repmat([0],1,30);repmat([0],1, 30)],15,1)
A(15,1) = 1
A(15,29) = 1
%obst 1---------------------
A(13,14:16) = 2
A(14:16,14) = 2
A(17,14:16) = 2
A(14:16,16) = 2
% ---------------------------

%obst 2 ---------------------
A(14,7:8) = 2
A(15,7:8) = 2
A(16,7:8) = 2

%obst 3 --------------------
% A(14,19:20) = 2
% A(15,19:20) = 2
% A(16,19:20) = 2

% A(20, 21:24) = 2
A(30,30) = 5

% Create title
title('Scenario');

title('Obstacle scenario');
surface(A);


