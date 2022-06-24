% 
%Para 30 x 30 ------------------------------------------------------

subplot(5,2,[1 2 3 4]);
title('UAV path obstacle [1 x obstacle]');
A = repmat([repmat([0],1,30);repmat([0],1, 30)],15,1)
% A(13:15,15) = 1

A(15,1) = 1
A(15,29) = 1
A(13,14:16) = 2
A(14:16,14) = 2

A(17,14:16) = 2
A(14:16,16) = 2
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

    
path_uav = [15, 45, 74, 105, 134, 164, 193, 222, 253, 284, 313, 343, 373, 402, 432, 462, 492, 523, 554, 585, 615, 646, 675, 704, 735, 765, 795, 824, 855, 885]
grid_vet(path_uav) = 4
A = reshape(grid_vet,30,30)


hold on 
z_max = max(max(get(h,'Zdata')))
[l, c]=find(A==4)
line(c,l,ones(1,length(unique(path_uav))),'DisplayName','Simple Q-learning','LineStyle','--','Marker','hexagram','LineWidth',2,'Color',[0.635294139385223 0.0784313753247261 0.184313729405403])

hold on
A = repmat([repmat([0],1,30);repmat([0],1, 30)],15,1)
grid_vet = A(:)'
path_uav_q_egreed = [15, 45, 74, 103, 132, 162, 193, 222, 253, 284, 313, 343, 373, 402, 432, 462, 492, 523, 554, 585, 615, 646, 675, 704, 735, 765, 795, 824, 855, 884]
grid_vet(path_uav_q_egreed) = 5

A = reshape(grid_vet,30,30)

[l_egreedy, c_egreedy]=find(A==5)
line(c_egreedy,l_egreedy,ones(1,length(unique(path_uav_q_egreed))),'DisplayName','Q-learning egreedy','LineStyle',':','Marker','hexagram','LineWidth',2,'Color',[0 1 0])

hold on

A = repmat([repmat([0],1,30);repmat([0],1, 30)],15,1)
grid_vet = A(:)'
path_uav_sarsa = [15, 45, 75, 105, 135, 165, 195, 224, 254, 284, 315, 345, 375, 405, 404, 403, 402, 433, 432, 463, 462, 493, 523, 554, 585, 615, 646, 675, 704, 735, 765, 794, 824, 854, 885] 
grid_vet(path_uav_sarsa) = 6

A = reshape(grid_vet,30,30)

[l_sarsa, c_sarsa]=find(A==6)
line(c_sarsa,l_sarsa,ones(1,length(unique(path_uav_sarsa))),'DisplayName','Sarsa','LineStyle',':','Marker','hexagram','LineWidth',2,'Color',[0 0 1])




%q_learning_simple ---

subplot(4,2,5);
A = repmat([repmat([0],1,30);repmat([0],1, 30)],15,1)
A(15,1) = 1
A(15,29) = 1
A(13,14:16) = 2
A(14:16,14) = 2

A(17,14:16) = 2
A(14:16,16) = 2
% A(20, 21:24) = 2


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
A(13,14:16) = 2
A(14:16,14) = 2

A(17,14:16) = 2
A(14:16,16) = 2

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
A(13,14:16) = 2
A(14:16,14) = 2

A(17,14:16) = 2
A(14:16,16) = 2

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
A(13,14:16) = 2
A(14:16,14) = 2

A(17,14:16) = 2
A(14:16,16) = 2
% A(20, 21:24) = 2
A(30,30) = 5

% Create title
title('Scenario');

title('Obstacle scenario');
surface(A);


