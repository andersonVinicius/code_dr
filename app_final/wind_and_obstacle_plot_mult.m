% 
%Para 30 x 30 ------------------------------------------------------

subplot(5,2,[1 2 3 4]);
title('Simple Q-learning x Q-learning egreedy x Sarsa');
A = repmat([repmat([0],1,30);repmat([0],1, 30)],15,1)
% A(13:15,15) = 1

A(15,1) = 1
A(15,29) = 1
A(5,12:15)= 2
A(3:5,15)= 2
A(24:25, 23:28) = 2
A(5:6,5:6) = 2
A(10:11,10:11) = 2
% A(15:16, 22:24) = 2
A(11:19, 15) = 2
A(11:15, 14) = 2
A(15,7:8) = 2
A(25,5:9) = 2
A(21:25,9) = 2
A(6, 21:25) = 2
A(6:9, 21) = 2
A(17:20, 21) = 2
A(20, 21:24) = 2
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

    
path_uav = [15, 45, 75, 106, 137, 168, 198, 228, 259, 290, 320, 351, 381, 411, 440, 469, 498, 528, 557, 586, 615, 644, 643, 673, 704, 733, 734, 765, 794, 825, 855, 885]
grid_vet(path_uav) = 4
A = reshape(grid_vet,30,30)


hold on 
z_max = max(max(get(h,'Zdata')))
[l, c]=find(A==4)
line(c,l,ones(1,length(unique(path_uav))),'DisplayName','Simple Q-learning','LineStyle','--','Marker','hexagram','LineWidth',2,'Color',[0.635294139385223 0.0784313753247261 0.184313729405403])

hold on
A = repmat([repmat([0],1,30);repmat([0],1, 30)],15,1)
grid_vet = A(:)'
path_uav_q_egreed = [15, 45, 74, 105, 134, 164, 193, 222, 253, 284, 315, 345, 375, 406, 435, 434, 433, 432, 431, 430, 459, 489, 519, 550, 551, 582, 613, 643, 673, 704, 735, 765, 795, 825, 855, 884, 885]
grid_vet(path_uav_q_egreed) = 5

A = reshape(grid_vet,30,30)

[l_egreedy, c_egreedy]=find(A==5)
line(c_egreedy,l_egreedy,ones(1,length(unique(path_uav_q_egreed))),'DisplayName','Q-learning egreedy','LineStyle',':','Marker','hexagram','LineWidth',2,'Color',[0 1 0])

hold on

A = repmat([repmat([0],1,30);repmat([0],1, 30)],15,1)
grid_vet = A(:)'
path_uav_sarsa = [15, 45, 75, 106, 136, 165, 195, 194, 225, 224, 255, 285, 315, 345, 375, 405, 404, 403, 402, 401, 400, 431, 430, 461, 492, 523, 554, 585, 615, 645, 676, 705, 706, 736, 766, 796, 826, 855, 854, 853, 884] 
grid_vet(path_uav_sarsa) = 6

A = reshape(grid_vet,30,30)

[l_sarsa, c_sarsa]=find(A==6)
line(c_sarsa,l_sarsa,ones(1,length(unique(path_uav_sarsa))),'DisplayName','Sarsa','LineStyle',':','Marker','hexagram','LineWidth',2,'Color',[0 0 1])




%q_learning_simple ---

subplot(4,2,5);
A = repmat([repmat([0],1,30);repmat([0],1, 30)],15,1)
A(15,1) = 1
A(15,29) = 1
A(5,12:15)= 2
A(3:5,15)= 2
A(24:25, 23:28) = 2
A(5:6,5:6) = 2
A(10:11,10:11) = 2
% A(15:16, 22:24) = 2
A(11:19, 15) = 2
A(11:15, 14) = 2
A(15,7:8) = 2
A(25,5:9) = 2
A(21:25,9) = 2
A(6, 21:25) = 2
A(6:9, 21) = 2
A(17:20, 21) = 2
A(20, 21:24) = 2
grid_vet = A(:)'
grid_vet(path_uav) = 4
A = reshape(grid_vet,30,30)
% Create axes



title('Path planing Simple Q-learning');

surface(A);
% view(axes1b,[90.4000000000001 -90]);


%-------------------------------------------------------------
%q-learning egreedy
subplot(4,2,6);
A = repmat([repmat([0],1,30);repmat([0],1, 30)],15,1)
A(15,1) = 1
A(15,29) = 1
A(5,12:15)= 2
A(3:5,15)= 2
A(24:25, 23:28) = 2
A(5:6,5:6) = 2
A(10:11,10:11) = 2
% A(15:16, 22:24) = 2
A(11:19, 15) = 2
A(11:15, 14) = 2
A(15,7:8) = 2
A(25,5:9) = 2
A(21:25,9) = 2
A(6, 21:25) = 2
A(6:9, 21) = 2
A(17:20, 21) = 2
A(20, 21:24) = 2
grid_vet = A(:)'
path_uav = path_uav_q_egreed
grid_vet(path_uav) = 5
A = reshape(grid_vet,30,30)
% Create axes

title('Path planing Q-learning egreedy');

surface(A);
% view(axes1c,[90.4000000000001 -90]);

%------------------------------------------------------------
%SARSA

%q-learning egreedy

subplot(4,2, 7);
A = repmat([repmat([0],1,30);repmat([0],1, 30)],15,1)
A(15,1) = 1
A(15,29) = 1
A(5,12:15)= 2
A(3:5,15)= 2
A(24:25, 23:28) = 2
A(5:6,5:6) = 2
A(10:11,10:11) = 2
% A(15:16, 22:24) = 2
A(11:19, 15) = 2
A(11:15, 14) = 2
A(15,7:8) = 2
A(25,5:9) = 2
A(21:25,9) = 2
A(6, 21:25) = 2
A(6:9, 21) = 2
A(17:20, 21) = 2
A(20, 21:24) = 2
grid_vet = A(:)'
path_uav = path_uav_sarsa
grid_vet(path_uav) = 6
A = reshape(grid_vet,30,30)

% Create title
title('Path planing Sarsa');

surface(A);
% view(axes1d,[90.4000000000001 -90]);

%cenario original 
subplot(4,2,8);

A = repmat([repmat([0],1,30);repmat([0],1, 30)],15,1)
A(15,1) = 1
A(15,29) = 1
A(5,12:15)= 2
A(3:5,15)= 2
A(24:25, 23:28) = 2
A(5:6,5:6) = 2
A(10:11,10:11) = 2
% A(15:16, 22:24) = 2
A(11:19, 15) = 2
A(11:15, 14) = 2
A(15,7:8) = 2
A(25,5:9) = 2
A(21:25,9) = 2
A(6, 21:25) = 2
A(6:9, 21) = 2
A(17:20, 21) = 2
A(20, 21:24) = 2
A(30,30) = 5

% Create title
title('Scenario');

title('Obstacle scenario');
surface(A);


