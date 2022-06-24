
%Para 30 x 30 ------------------------------------------------------
% Create figure
figure1 = figure;

% Create axes
axes1 = axes('Parent',figure1);
hold(axes1,'on');

A = repmat([repmat([0],1,30);repmat([0],1, 30)],15,1)
% A(13:15,15) = 1

A(15,1) = 1
A(15,29) = 1
A(13,14:16) = 2
A(14:16,14) = 2

A(17,14:16) = 2
A(14:16,16) = 2

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
%ini
% pcolor(A)
surface(A,'Parent',axes1,'AlignVertexCenters','on',...
    'CData',A);
box(axes1,'on');
view(axes1,[90.4000000000001 -90]);

grid_vet = A(:)'
grids_ids = find(grid_vet==2)
vet_to_py = ' '
for i=1:length(grids_ids)
    vet_to_py=strcat(num2str(grids_ids(i)),',', vet_to_py) 
end    

    
path_uav = [15, 45, 75, 105, 135, 165, 195, 225, 255, 285, 315, 344, 373, 402, 432, 462, 493, 524, 555, 585, 615, 645, 675, 705, 735, 765, 795, 825, 855, 885] 
grid_vet(path_uav) = 4

A = reshape(grid_vet,30,30)

figure1b = figure;

% Create axes
axes1b = axes('Parent',figure1b);
hold(axes1b,'on');


surface(A,'Parent',axes1b,'AlignVertexCenters','on',...
    'CData',A);
view(axes1b,[90.4000000000001 -90]);
