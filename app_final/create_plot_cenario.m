% 
%Para 30 x 30 ------------------------------------------------------
% Create figure
figure1 = figure;

% Create title
title('Simple Q-lerning x Q-learning egreedy x Sarsa');
% Create axes
axes1 = axes('Parent',figure1);
hold(axes1,'on');

A = repmat([repmat([0],1,30);repmat([0],1, 30)],15,1)
% A(13:15,15) = 1

A(15,1) = 1
A(15,29) = 1
% A(5,12:15)= 2
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
% for i=1:29
    A(15,1:29)= 2
% end
%ini
% pcolor(A)
h=surface(A,'Parent',axes1,'AlignVertexCenters','on',...
    'CData',A);
box(axes1,'on');
% view(axes1,[90.4000000000001 -90]);

grid_vet = A(:)'
grids_ids = find(grid_vet==2)
vet_to_py = ' '
for i=1:length(grids_ids)
    vet_to_py=strcat(num2str(grids_ids(i)),',', vet_to_py) 
end    

    
% path_uav = [15, 45, 75, 105, 135, 165, 196, 226, 255, 285, 316, 347, 378, 409, 440, 469, 498, 527, 526, 555, 584, 613, 644, 674, 705, 735, 765, 794, 825, 855, 885]
% grid_vet(path_uav) = 4
% A = reshape(grid_vet,30,30)
% 
% 
% hold on 
% z_max = max(max(get(h,'Zdata')))
% [l, c]=find(A==4)
% line(c,l,z_max*ones(1,length(unique(path_uav))),'DisplayName','Simple Q-learning','LineStyle','--','Marker','hexagram','LineWidth',2,'Color',[0.635294139385223 0.0784313753247261 0.184313729405403])
% 
% hold on
% A = repmat([repmat([0],1,30);repmat([0],1, 30)],15,1)
% grid_vet = A(:)'
% path_uav_q_egreed = [15, 45, 75, 105, 135, 165, 196, 226, 255, 285, 315, 345, 375, 406, 435, 434, 433, 432, 431, 430, 461, 491, 522, 553, 584, 615, 646, 645, 675, 705, 735, 765, 795, 825, 855, 884, 885] 
% grid_vet(path_uav_q_egreed) = 5
% 
% A = reshape(grid_vet,30,30)
% 
% [l_egreedy, c_egreedy]=find(A==5)
% line(c_egreedy,l_egreedy,z_max*ones(1,length(unique(path_uav_q_egreed))),'DisplayName','Q-learning egreedy','LineStyle',':','Marker','hexagram','LineWidth',2,'Color',[0 1 0])
% 
% hold on
% 
% A = repmat([repmat([0],1,30);repmat([0],1, 30)],15,1)
% grid_vet = A(:)'
% path_uav_sarsa = [15, 45, 76, 105, 136, 135, 165, 195, 194, 225, 224, 254, 284, 315, 345, 376, 405, 404, 403, 402, 401, 400, 431, 430, 461, 492, 493, 524, 555, 584, 615, 645, 676, 705, 706, 736, 766, 796,885] 
% grid_vet(path_uav_sarsa) = 6
% 
% A = reshape(grid_vet,30,30)
% 
% [l_sarsa, c_sarsa]=find(A==6)
% line(c_sarsa,l_sarsa,z_max*ones(1,length(unique(path_uav_sarsa))),'DisplayName','Sarsa','LineStyle',':','Marker','hexagram','LineWidth',2,'Color',[0 0 1])
% 
% 
% 
% 
% %q_learning_simple ---
% 
% figure1b = figure;
% A = repmat([repmat([0],1,30);repmat([0],1, 30)],15,1)
% A(15,1) = 1
% A(15,29) = 1
% A(5,12:15)= 2
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
% grid_vet = A(:)'
% grid_vet(path_uav) = 4
% A = reshape(grid_vet,30,30)
% % Create axes
% axes1b = axes('Parent',figure1b);
% hold(axes1b,'on');
% 
% 
% title('Path planing Simple Q-learning');
% 
% surface(A,'Parent',axes1b,'AlignVertexCenters','on',...
%     'CData',A);
% view(axes1b,[90.4000000000001 -90]);
% 
% 
% %-------------------------------------------------------------
% %q-learning egreedy
% 
% figure1c = figure;
% A = repmat([repmat([0],1,30);repmat([0],1, 30)],15,1)
% A(15,1) = 1
% A(15,29) = 1
% A(5,12:15)= 2
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
% grid_vet = A(:)'
% path_uav = path_uav_q_egreed
% grid_vet(path_uav) = 5
% A = reshape(grid_vet,30,30)
% % Create axes
% axes1c = axes('Parent',figure1c);
% hold(axes1c,'on');
% 
% title('Path planing Q-learning egreedy');
% 
% surface(A,'Parent',axes1c,'AlignVertexCenters','on',...
%     'CData',A);
% view(axes1c,[90.4000000000001 -90]);
% 
% %------------------------------------------------------------
% %SARSA
% 
% %q-learning egreedy
% 
% figure1d = figure;
% A = repmat([repmat([0],1,30);repmat([0],1, 30)],15,1)
% A(15,1) = 1
% A(15,29) = 1
% A(5,12:15)= 2
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
% grid_vet = A(:)'
% path_uav = path_uav_sarsa
% grid_vet(path_uav) = 6
% A = reshape(grid_vet,30,30)
% % Create axes
% axes1d = axes('Parent',figure1d);
% hold(axes1d,'on');
% % Create title
% title('Path planing Sarsa');
% 
% surface(A,'Parent',axes1d,'AlignVertexCenters','on',...
%     'CData',A);
% view(axes1d,[90.4000000000001 -90]);
% 
% %cenario original 
% 
% figure1e = figure;
% A = repmat([repmat([0],1,30);repmat([0],1, 30)],15,1)
% A(15,1) = 1
% A(15,29) = 1
% A(5,12:15)= 2
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
% 
% % Create axes
% axes1e = axes('Parent',figure1e);
% hold(axes1e,'on');
% 
% % Create title
% title('Cenario original');
% 
% surface(A,'Parent',axes1e,'AlignVertexCenters','on',...
%     'CData',A);

% 
% %Para 20 x 20 ------------------------------------------------------
% 
% 
% figure2 = figure;
% 
% % Create axes
% axes2 = axes('Parent',figure2);
% hold(axes1,'on');
% 
% A = repmat([repmat([0],1,20);repmat([0],1, 20)],10,1)
% 
% 
% A(10,1) = 1
% A(10,19) = 1
% A(5,12:10)= 2
% A(3:5,10)= 2
% A(15:18, 17:18) = 2
% A(5:6,5:6) = 2
% A(10:11,10:11) = 2
% A(15,5:9) = 2
% A(10:17, 10) = 2
% A(11:10, 9) = 2
% A(15,5:9) = 2
% A(19,5:9) = 2
% A(15:18,9) = 2
% A(6, 13:17) = 2
% A(6:9, 19) = 2
% A(15:18, 18) = 2
% A(15, 17:19) = 2
% 
% surface(A,'Parent',axes2,'AlignVertexCenters','on',...
%     'CData',A);

% %Para 15 x 15 ------------------------------------------------------
% figure3 = figure;
% 
% % Create axes
% axes3 = axes('Parent',figure3);
% hold(axes3,'on');
% 
% A = repmat([repmat([0],1,15);repmat([0],1, 15)],8,1)
% 
% 
% A(8,1) = 1
% A(8,14) = 1
% A(7:8,7:8) = 2
% A(5, 9) = 2
% A(9, 5) = 2
% A(9:13,11) = 2
% A(2,3:5) = 2
% A(3:5,2) = 2
% A(13,2:5) = 2
% A(12:13,2) = 2
% A(3,11:13) = 2
% A(3:4,12) = 2
% 
% 
% 
% surface(A,'Parent',axes3,'AlignVertexCenters','on',...
%     'CData',A);

%Para 10 x 10 ------------------------------------------------------

% A = repmat([repmat([0],1,10);repmat([0],1, 10)],5,1)
% 
% 
% A(5,1) = 1
% A(5,9) = 1
% 
% A(5,5:6) = 2
% A(5:6, 5) = 2
% A(3,5) = 2
% A(2,2:4) = 2
% A(8,8:9)= 2
% A(7:8,2:3)= 2
% 
% 
% figure4a = figure;
% 
% % Create axes
% axes4a = axes('Parent',figure4a);
% hold(axes4a,'on');
% 
% 
% surface(A,'Parent',axes4a,'AlignVertexCenters','on',...
%     'CData',A);
% view(axes4a,[90.4000000000001 -90]);
% 
% 
% 
% grid_vet = A(:)'
% grids_ids = find(grid_vet==2)
% 
% path_uav = [5, 15, 25, 35, 44, 54, 65, 75, 85, 95] 
% grid_vet(path_uav) = 4
% 
% A = reshape(grid_vet,10,10)
% 
% figure4 = figure;
% 
% % Create axes
% axes4 = axes('Parent',figure4);
% hold(axes4,'on');
% 
% 
% surface(A,'Parent',axes4,'AlignVertexCenters','on',...
%     'CData',A);
% view(axes4,[90.4000000000001 -90]);

min = 10000000
os_menore = []
for i = 1:100
    if x30stepsforep(i)<min
        min = x30stepsforep(i)
        os_menore(i) = min
    else
        os_menore(i) = min
    end
    
end

aux_mean_1000_delta = []
for i = 1:1000:49000
    
   aux_mean_1000_delta(i) = mean(x30deltaforep(i:i+1000))
           
end

