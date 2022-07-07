n=5;
[path_uav, path_uav_egreedy, path_uav_sarsa, tipo_vento, tipo_obstaculo] = obter_path_para_cada_experimento(n);
load(obter_points_alta_velo_vento(tipo_vento));
cenario = tipo_obstaculo;
% Create figure
figure1 = figure;
figure1.Position = [1000 2600 900 2600];

axes1 = axes('Parent',figure1,...
    'Position',[0.131098901098901 0.77673011198198 0.777197802197802 0.198217858881709]);
axis off
hold(axes1,'on');

% subplot1 = subplot(9,2,[1 2 3 4],'Parent',figure1);
% hold(subplot1,'on');
title(strcat('Scenario[',num2str(n),']'));
A = obter_posicao_obstaculos(cenario);

h=surface(A,'Parent',axes1,'DisplayName','');
% box(axes1,'on');
% view(axes1,[90.4000000000001 -90]);

grid_vet = A(:)';
grids_ids = find(grid_vet==2);
vet_to_py = ' ';
for i=1:length(grids_ids)
    vet_to_py=strcat(num2str(grids_ids(i)),',', vet_to_py); 
end    

 
grid_vet(path_uav) = 4;
A = reshape(grid_vet,30,30);


hold on 
z_max = max(max(get(h,'Zdata')));
[l, c]=find(A==4);
line(c,l,ones(1,length(unique(path_uav))),'Parent',axes1,'DisplayName','Simple Q-learning','LineStyle','--','Marker','hexagram','LineWidth',2,'Color',[0.635294139385223 0.0784313753247261 0.184313729405403]);

hold on
A = repmat([repmat([0],1,30);repmat([0],1, 30)],15,1);
grid_vet = A(:)';
grid_vet(path_uav_egreedy) = 5;

A = reshape(grid_vet,30,30);

[l_egreedy, c_egreedy]=find(A==5);
line(c_egreedy,l_egreedy,ones(1,length(unique(path_uav_egreedy))),'Parent',axes1,'DisplayName','Q-learning egreedy','LineStyle',':','Marker','hexagram','LineWidth',2,'Color',[0 1 0]);

hold on

A = repmat([repmat([0],1,30);repmat([0],1, 30)],15,1);
grid_vet = A(:)';
grid_vet(path_uav_sarsa) = 6;

A = reshape(grid_vet,30,30);

[l_sarsa, c_sarsa]=find(A==6);
line(c_sarsa,l_sarsa,ones(1,length(unique(path_uav_sarsa))),'Parent',axes1,'DisplayName','Sarsa','LineStyle',':','Marker','hexagram','LineWidth',2,'Color',[0.952941179275513 0.87058824300766 0.733333349227905]);

view([0.4 90]);
% Create legend
legend1 = legend(axes1,'show');
set(legend1,'Orientation','horizontal','Location','northeast');


%q_learning_simple ---
% Create axes
axes2 = axes('Parent',figure1,...
    'Position',[0.13 0.577316513761468 0.334659090909091 0.160756880733945]);
hold(axes2,'on');

A = obter_posicao_obstaculos(cenario);


grid_vet = A(:)';
grid_vet(path_uav) = 4;
A = reshape(grid_vet,30,30);
% Create axes


title('Path planing Simple Q-learning WO');

surface(A,'Parent',axes2);

%-------------------------------------------------------------
%q-learning egreedy---------------------------------------------
% Create axes
axes3 = axes('Parent',figure1,...
    'Position',[0.570340909090909 0.577316513761468 0.334659090909091 0.160756880733945]);
hold(axes3,'on');

A = obter_posicao_obstaculos(cenario);

grid_vet = A(:)';
% path_uav = path_uav_egreedy
grid_vet(path_uav_egreedy) = 5;
A = reshape(grid_vet,30,30);
% Create axes

title('Path planing Q-learning egreedy WO');

surface(A,'Parent', axes3);
% view(axes1c,[90.4000000000001 -90]);

%------------------------------------------------------------
%SARSA---------------------------------------------------------
% Create axes
axes4 = axes('Parent',figure1,...
    'Position',[0.349954648526078 0.37582175008831 0.334659090909091 0.160756880733947]);
hold(axes4,'on');

A = obter_posicao_obstaculos(cenario);

grid_vet = A(:)';
% path_uav = path_uav_sarsa
grid_vet(path_uav_sarsa) = 6;
A = reshape(grid_vet,30,30);

% Create title
title('Path planing Sarsa WO');

surface(A,'Parent',axes4);

% Create axes
axes5 = axes('Parent',figure1,...
    'Position',[0.127450980392157 0.0894901144640999 0.777549019607843 0.246634335411319]);
hold(axes5,'on');

title('UAV path analyze wind speed [Mult obstacle]');
% colormap(Parula);
% hold(axes1,'on');


wind_amb_aux = windambiente;
wind_amb_aux(path_uav) = -1;

wind_matrix = reshape(windambiente,30,30);
wind_matrix_aux = reshape(wind_amb_aux,30,30);

[l, c]=find(wind_matrix_aux==-1);



h=surface(wind_matrix,'Parent',axes5,'DisplayName','');
shading interp;
% box(axes1,'on');

hold on 
z_max = max(max(get(h,'Zdata')));
line(c,l,z_max*ones(1,length(path_uav)),'Parent',axes5 ,'DisplayName','Simple Q-learning','LineStyle','--','Marker','hexagram','LineWidth',2,'Color',[0.635294139385223 0.0784313753247261 0.184313729405403]);

hold on

wind_amb_aux = windambiente;
wind_amb_aux(path_uav_egreedy) = -2;
wind_matrix_aux = reshape(wind_amb_aux,30,30);
[l_egreedy, c_egreedy]=find(wind_matrix_aux==-2);
line(c_egreedy,l_egreedy, z_max*ones(1,length(path_uav_egreedy)),'Parent',axes5 ,'DisplayName','Q-learning egreedy','LineStyle',':','Marker','hexagram','LineWidth',2,'Color',[0 1 0]);
% view(axes1,[90.4000000000001 -90]);

hold on

wind_amb_aux = windambiente;
wind_amb_aux(path_uav_sarsa) = -3;
wind_matrix_aux = reshape(wind_amb_aux,30,30);
[l_sarsa, c_sarsa]=find(wind_matrix_aux==-3);
line(c_sarsa,l_sarsa,z_max*ones(1,length(path_uav_sarsa)),'Parent',axes5,'DisplayName','Sarsa','Marker','hexagram','LineWidth',2,'Color',[0.952941179275513 0.87058824300766 0.733333349227905]);




view(axes5,[1.36779476633819e-13 90]);
% Create colorbar
colorbar('peer',axes5,'southoutside','Position',...
    [0.135057099762982 0.0541103017689909 0.767032967032967 0.0110564723712045]);
% Create legend
legend2 = legend(axes5,'show');
set(legend2,'Orientation','horizontal','Location','northeast');
% Create textarrow
annotation(figure1,'textarrow',[0.197488584474886 0.157534246575342],...
    [0.91991571279917 0.879292403746101],'Color',[1 1 1],'String',{'START'},...
    'FontWeight','bold');

% Create textarrow
annotation(figure1,'textarrow',[0.855022831050228 0.905895691609977],...
    [0.825222684703434 0.875816993464053],'Color',[1 1 1],'String',{'TARGET'},...
    'FontWeight','bold');

% Create textarrow
annotation(figure1,'textarrow',[0.263260887927282 0.479942693409742],...
    [0.800482206942208 0.853157121879589],'Color',[1 1 1],'String',{'OBSTACLE'},...
    'FontWeight','bold',...
    'FontSize',9);

% Create textbox
annotation(figure1,'textbox',...
    [0.444519972091401 0.0144219324913457 0.161637362637362 0.0249739854318419],...
    'String','Wind Speed (m/s)',...
    'LineStyle','none',...
    'FitBoxToText','off');

function A = obter_posicao_obstaculos(n)
    switch n
        case 1
            disp('multiplos obstaculo homogeneos no centro ')
            A = repmat([repmat([0],1,30);repmat([0],1, 30)],15,1);
            A(15,1) = 1;

            A(15,29) = 1;

                for i= 9:2:22
                    for j=9:2:22
                    A(i,j)= 2;
                    end
                end
        case 2
            disp('Um obstaculo')
            A = repmat([repmat([0],1,30);repmat([0],1, 30)],15,1);
            % A(13:15,15) = 1

            A(15,1) = 1;
            A(15,29) = 1;
            A(13,14:16) = 2;
            A(14:16,14) = 2;

            A(17,14:16) = 2;
            A(14:16,16) = 2;
        case 3
            disp('dois obstaculos')
            A = repmat([repmat([0],1,30);repmat([0],1, 30)],15,1);
            % A(13:15,15) = 1

            A(15,1) = 1;
            A(15,29) = 1;
            %obst 1---------------------
            A(13,14:16) = 2;
            A(14:16,14) = 2;
            A(17,14:16) = 2;
            A(14:16,16) = 2;
            % ---------------------------

            %obst 2 ---------------------
            A(12,7:8) = 3;
            A(13,7:8) = 3;
            A(14,7:8) = 3;
            A(15,7:8) = 3;
            A(16,7:8) = 3;
        case 4
            disp('Muultiplos obstaculos heterogeneos')
            A = repmat([repmat([0],1,30);repmat([0],1, 30)],15,1);
            % A(13:15,15) = 1

            A(15,1) = 1;
            A(15,29) = 1;
            A(5,12:15)= 2;
            A(3:5,15)= 2;
            A(24:25, 23:28) = 2;
            A(5:6,5:6) = 2;
            A(10:11,10:11) = 2;
            % A(15:16, 22:24) = 2
            A(11:19, 15) = 2;
            A(11:15, 14) = 2;
            A(15,7:8) = 2;
            A(25,5:9) = 2;
            A(21:25,9) = 2;
            A(6, 21:25) = 2;
            A(6:9, 21) = 2;
            A(17:20, 21) = 2;
            A(20, 21:24) = 2;
    end
end

function wind_style = obter_points_alta_velo_vento(n)
    switch(n)
        case 1
            disp('aleatorio Wind')
            wind_style = 'windambiente.mat';
        case 2
            disp('Center wind')
            wind_style = 'center_points_max_wind_speed.mat';
        case 3
            disp('metade superior wind')
            wind_style = 'upper half_points_max_wind_speed.mat';
    end
end

function [path_uav, path_uav_egreed, path_uav_sarsa, tipo_vento, tipo_obstaculo] = obter_path_para_cada_experimento(n)
    switch(n)
        case 1
            disp('Experimento com 1 obstaculo e velocidade do vento aleatoria')
            path_uav = [15, 45, 74, 105, 134, 164, 193, 222, 253, 284, 313, 343, 373, 402, 432, 462, 492, 523, 554, 585, 615, 646, 675, 704, 735, 765, 795, 824, 855, 885];
            path_uav_egreed = [15, 45, 74, 103, 132, 162, 193, 222, 253, 284, 313, 343, 373, 402, 432, 462, 492, 523, 554, 585, 615, 646, 675, 704, 735, 765, 795, 824, 855, 884];
            path_uav_sarsa = [15, 45, 75, 105, 135, 165, 195, 224, 254, 284, 315, 345, 375, 405, 404, 403, 402, 433, 432, 463, 462, 493, 523, 554, 585, 615, 646, 675, 704, 735, 765, 794, 824, 854, 885]; 
            tipo_vento = 1;
            tipo_obstaculo = 2;
        case 2
            disp('Experimento com 2 obstaculo e velocidade do vento aleatoria')
            path_uav = [15, 45, 75, 106, 137, 168, 198, 228, 257, 286, 315, 344, 373, 402, 432, 462, 492, 523, 554, 585, 615, 646, 675, 704, 735, 765, 795, 824, 855, 885];
            path_uav_egreed = [15, 45, 75, 106, 137, 168, 198, 228, 259, 290, 320, 349, 379, 408, 438, 468, 498, 528, 557, 586, 615, 646, 675, 704, 735, 765, 795, 824, 855, 885];
            path_uav_sarsa = [15, 46, 76, 105, 136, 165, 195, 194, 193, 192, 191, 222, 221, 251, 282, 313, 344, 373, 404, 403, 402, 433, 432, 463, 462, 493, 524, 554, 585, 616, 645, 676, 706, 735, 765, 795, 826, 855, 885];
            tipo_vento = 1;
            tipo_obstaculo = 3;
        case 3
            disp('Experimento com varios obstuculos heterogenos com vento aleatorio')
            path_uav = [15, 45, 75, 106, 137, 168, 198, 228, 259, 290, 320, 351, 381, 411, 440, 469, 498, 528, 557, 586, 615, 644, 643, 673, 704, 733, 734, 765, 794, 825, 855, 885];
            path_uav_egreed = [15, 45, 74, 105, 134, 164, 193, 222, 253, 284, 315, 345, 375, 406, 435, 434, 433, 432, 431, 430, 459, 489, 519, 550, 551, 582, 613, 643, 673, 704, 735, 765, 795, 825, 855, 884, 885];
            path_uav_sarsa = [15, 45, 75, 106, 136, 165, 195, 194, 225, 224, 255, 285, 315, 345, 375, 405, 404, 403, 402, 401, 400, 431, 430, 461, 492, 523, 554, 585, 615, 645, 676, 705, 706, 736, 766, 796, 826, 855, 854, 853, 884];
            tipo_vento = 1;
            tipo_obstaculo = 4;
        case 4
            disp('Experimento com varios obstuculos homogeneos no centro, com alta influencia do vento no centro')
            path_uav = [15, 45, 74, 105, 106, 137, 168, 198, 227, 258, 289, 320, 349, 380, 411, 440, 469, 498, 529, 560, 589, 618, 647, 678, 708, 737, 766, 795, 824, 855, 884, 885];
            path_uav_egreed =  [15, 45, 74, 105, 106, 137, 168, 198, 227, 258, 289, 320, 349, 380, 411, 440, 471, 502, 533, 562, 591, 620, 649, 678, 708, 737, 766, 795, 824, 855, 884];
            path_uav_sarsa = [15, 45, 75, 106, 136, 166, 195, 225, 256, 285, 314, 345, 376, 405, 435, 434, 465, 495, 494];
            tipo_vento = 2
            tipo_obstaculo = 1
        case 5
            disp('Experimento com varios obstuculos homogeneos no centro, com alta influencia do vento na metade superior do cenario')
            path_uav = [15, 45, 74, 105, 136, 165, 194, 225, 254, 284, 314, 343, 372, 401, 430, 459, 488, 519, 548, 579, 610, 640, 671, 702, 733, 764, 794, 825, 855, 885];
            path_uav_egreed =  [15, 45, 74, 105, 136, 165, 194, 225, 254, 283, 312, 341, 370, 399, 428, 459, 488, 518, 547, 578, 608, 639, 670, 701, 732, 763, 794, 825, 855, 885]; 
            path_uav_sarsa = [15, 45, 74, 104, 135, 164, 193, 224, 254, 284, 314, 345, 375, 374, 405, 435, 434, 464, 494, 524, 554, 585, 614, 645, 675, 704, 734, 765, 795, 826, 855, 885];
            tipo_vento = 3;
            tipo_obstaculo = 1;
        case 7
    end
end
    
    
    
    
    