config_grid = {'5','10','15', '20', '30'} 
% eleito = 1;







plot_energy_5 = [];
plot_energy_10 = [];
plot_energy_15 = [];
plot_energy_20 = [];
plot_energy_30 = [];

for id_grid = 1:length(config_grid)
    
    path_naive = strcat('data_naive/',config_grid{id_grid},'_pontoDePartidaUavNewDistaceNaive.csv');
    path_sarsa = strcat('data_sarsa/',config_grid{id_grid},'_x_',config_grid{id_grid},'pontoDePartidaUavNewDistaceSarsa.csv');
    path_egreedy = strcat('data_egreedy/',config_grid{id_grid},'_x_',config_grid{id_grid},'_pontoDePartidaUavNewDistace.csv');
    path_simple_ql = strcat('data_simple_ql/',config_grid{id_grid},'_x_',config_grid{id_grid},'_pontoDePartidaUavNewDistaceSarsa.csv');
    
    paths = {path_naive, path_sarsa, ...
         path_egreedy, path_simple_ql
         };
    for path_id = 1:length(paths) 
        data = readtable(paths{path_id});
        mat_energy(path_id,:) = table2array(data(1,1:15));  
    end 
    set_all_config_energy(id_grid,:,:) = mat_energy
end



% Create figure
figure1 = figure;
figure1.Position = [1000 1000 1280 900]

% % Create axes
% axes1 = axes('Parent',figure1,...
%     'Position',[0.13 0.800677966101695 0.775 0.157741935483871]);
% hold(axes1,'on');
% plot_energy_5 (1:4,1:15)= set_all_config_energy(1,:,1:15)
% % Create multiple lines using matrix input to bar
% bar1=bar(plot_energy_5','Parent',axes1);
% set(bar1(1),'DisplayName','Naive',...
%     'FaceColor',[0.756862759590149 0.866666674613953 0.776470601558685]);
% set(bar1(2),'DisplayName','Sarsa',...
%     'FaceColor',[0.925490200519562 0.839215695858002 0.839215695858002]);
% set(bar1(3),'DisplayName','egreedy Q-learning',...
%     'FaceColor',[0.584313750267029 0.388235300779343 0.388235300779343]);
% set(bar1(4),'DisplayName','Simple Q-learning',...
%     'FaceColor',[0.729411780834198 0.831372559070587 0.95686274766922]);
% 
% 
% % Create ylabel
% ylabel('Energy consumed (J)');
% 
% % Create title
% title('Grid dimension 5 x 5');
% 
% box(axes1,'on');
% % Set the remaining axes properties
% set(axes1,'XTick',[1 2 3 4 5 6 7 8 9 10 11 12 13 14 15]);
% 
% %-----------------------------------------------------------------------------------------
% 
% % Create axes
% axes2 = axes('Parent',figure1,...
%     'Position',[0.13 0.628008474576271 0.775 0.124322033898305]);
% hold(axes2,'on');
% 
% plot_energy_10 (1:4,1:15)= set_all_config_energy(2,:,1:15)
% 
% % Create multiple lines using matrix input to bar
% bar2 = bar(plot_energy_10','Parent',axes2);
% 
% set(bar2(1),'DisplayName','Naive',...
%     'FaceColor',[0.756862759590149 0.866666674613953 0.776470601558685]);
% set(bar2(2),'DisplayName','Sarsa',...
%     'FaceColor',[0.925490200519562 0.839215695858002 0.839215695858002]);
% set(bar2(3),'DisplayName','Egreedy Q-learning',...
%     'FaceColor',[0.584313750267029 0.388235300779343 0.388235300779343]);
% set(bar2(4),'DisplayName','Simple Q-learning',...
%     'FaceColor',[0.729411780834198 0.831372559070587 0.95686274766922]);
% 
% % Create ylabel
% ylabel('Energy consumed (J)');
% 
% % Create title
% title('Grid dimension 10 x 10');
% 
% box(axes2,'on');
% % Set the remaining axes properties
% set(axes2,'XTick',[1 2 3 4 5 6 7 8 9 10 11 12 13 14 15]);
% 
% %-----------------------------------------------------------------------------------------
% 
% % Create axes
% axes3 = axes('Parent',figure1,...
%     'Position',[0.13 0.455338983050847 0.775 0.124322033898305]);
% hold(axes3,'on');
% 
% plot_energy_15 (1:4,1:15)= set_all_config_energy(3,:,1:15)
% 
% % Create multiple lines using matrix input to bar
% bar3=bar(plot_energy_15','Parent',axes3);
% 
% set(bar3(1),'DisplayName','Naive',...
%     'FaceColor',[0.756862759590149 0.866666674613953 0.776470601558685]);
% set(bar3(2),'DisplayName','Sarsa',...
%     'FaceColor',[0.925490200519562 0.839215695858002 0.839215695858002]);
% set(bar3(3),'DisplayName','Egreedy Q-learning',...
%     'FaceColor',[0.584313750267029 0.388235300779343 0.388235300779343]);
% set(bar3(4),'DisplayName','Simple Q-learning',...
%     'FaceColor',[0.729411780834198 0.831372559070587 0.95686274766922]);
% 
% % Create ylabel
% ylabel('Energy consumed (J)');
% 
% % Create title
% title('Grid dimension 15 x 15');
% 
% 
% box(axes3,'on');
% % Set the remaining axes properties
% set(axes3,'XTick',[1 2 3 4 5 6 7 8 9 10 11 12 13 14 15]);
% 
% %-----------------------------------------------------------------------------------------
% 
% % Create axes
% axes4 = axes('Parent',figure1,...
%     'Position',[0.13 0.282669491525424 0.775 0.124322033898305]);
% hold(axes4,'on');
% 
% plot_energy_20 (1:4,1:15) = set_all_config_energy(4,:,1:15)
% 
% % Create multiple lines using matrix input to bar
% bar4=bar(plot_energy_20','Parent',axes4);
% set(bar4(4),'DisplayName','Simple Q-learning',...
%     'FaceColor',[0.729411780834198 0.831372559070587 0.95686274766922]);
% set(bar4(3),'DisplayName','Egreedy Q-learning',...
%     'FaceColor',[0.584313750267029 0.388235300779343 0.388235300779343]);
% set(bar4(2),'DisplayName','Sarsa',...
%     'FaceColor',[0.925490200519562 0.839215695858002 0.839215695858002]);
% set(bar4(1),'DisplayName','Naive',...
%     'FaceColor',[0.756862759590149 0.866666674613953 0.776470601558685]);
% 
% % Create ylabel
% ylabel('Energy consumed (J)');
% 
% % Create title
% title('Grid dimension 20 x 20');
% 
% box(axes4,'on');
% % Set the remaining axes properties
% set(axes4,'XTick',[1 2 3 4 5 6 7 8 9 10 11 12 13 14 15]);

%-----------------------------------------------------------------------------------------


axes5 = axes('Parent',figure1,...
    'Position',[0.129161777032691 0.097202216066482 0.775 0.124322033898305]);
hold(axes5,'on');
plot_energy_30 (1:4,1:15) =  set_all_config_energy(5,:,1:15)
% Create multiple lines using matrix input to bar
bar5=bar(plot_energy_30','Parent',axes5);
set(bar5(4),'DisplayName','Simple Q-learning',...
    'FaceColor',[0.729411780834198 0.831372559070587 0.95686274766922]);
set(bar5(3),'DisplayName','Egreedy Q-learning',...
    'FaceColor',[0.584313750267029 0.388235300779343 0.388235300779343]);
set(bar5(2),'DisplayName','Sarsa',...
    'FaceColor',[0.925490200519562 0.839215695858002 0.839215695858002]);
set(bar5(1),'DisplayName','Naive',...
    'FaceColor',[0.756862759590149 0.866666674613953 0.776470601558685]);

% Create ylabel
ylabel('Distance (m)');

% Create title
title('Grid dimension 30 x 30');

box(axes5,'on');
% Set the remaining axes properties
set(axes5,'XTick',[1 2 3 4 5 6 7 8 9 10 11 12 13 14 15]);


% Create legend
legend1 = legend(axes4,'show');
set(legend1,...
    'Position',[0.288348700754401 0.951321279554937 0.440794698964384 0.0427381395562711],...
    'Orientation','horizontal',...
    'FontSize',10);
% Create textbox
annotation(figure1,'textbox',...
    [0.488845766974015 0.0155807365439094 0.0643813914501258 0.0424929178470255],...
    'String','ID UAV',...
    'LineStyle','none',...
    'FontSize',11,...
    'FitBoxToText','off');



%------------------------------------------------------------------------------------------


 %call barPlot
%  building_bar_energy(mat_energy, config_grid{1})

 % Create figure

% Graph settings

% subplot(5,2,[1 2]);
% plot_energy_5 (1:4,1:15)= set_all_config_energy(1,:,1:15)
% % Create multiple lines using matrix input to bar
% bar(plot_energy_5');
% 
% subplot(5, 2, [3 4]);
% plot_energy_5 (1:4,1:15)= set_all_config_energy(1,:,1:15)
% % Create multiple lines using matrix input to bar
% bar(plot_energy_5');
% subplot(5, 2, [5 6]);
% 
% plot_energy_5 (1:4,1:15)= set_all_config_energy(1,:,1:15)
% % Create multiple lines using matrix input to bar
% bar(plot_energy_5');
% 
% subplot(5, 2, [7 8]);
% plot_energy_5 (1:4,1:15)= set_all_config_energy(1,:,1:15)
% % Create multiple lines using matrix input to bar
% bar(plot_energy_5');
% 
% 
% subplot(5, 2, [9 10]);
% plot_energy_5 (1:4,1:15)= set_all_config_energy(1,:,1:15)
% % Create multiple lines using matrix input to bar
% bar(plot_energy_5');

% function [] = building_bar_energy(mat_energy, grid, figure1)
% 
%    
% 
%     % Create axes
%     axes1 = axes('Parent',figure1,...
%     'Position',[0.11449016100179 0.11 0.829338103756708 0.727696335078534]);
% hold(axes1,'on');
% 
%     bar1 = bar(mat_energy');
% 
%     set(bar1(4),'DisplayName','Simple Q-learning',...
%         'FaceColor',[0.39215686917305 0.474509805440903 0.635294139385223]);
%     set(bar1(3),'DisplayName','Egreedy Q-learning',...
%         'FaceColor',[0.529411792755127 0.317647069692612 0.317647069692612]);
%     set(bar1(2),'DisplayName','Sarsa',...
%         'FaceColor',[0.756862759590149 0.866666674613953 0.776470601558685]);
%     set(bar1(1),'DisplayName','naive',...
%         'FaceColor',[0.952941179275513 0.87058824300766 0.733333349227905]);
% 
%     % Create ylabel
%     ylabel('Energy consumed(j)');
% 
%     % Create xlabel
%     xlabel('ID UAV');
% 
%     box(axes1,'on');
%     % Set the remaining axes properties
%     set(axes1,'XTick',[1 2 3 4 5 6 7 8 9 10 11 12 13 14 15],'XTickLabel',...
%         {'1','2','3','4','5','6','7','8','9','10','11','12','13','14','15'},'YGrid',...
%         'on');
%     % Create legend
%     legend1 = legend(axes1,'show');
%     set(legend1,...
%         'Position',[0.284287393325817 0.885034906939582 0.435599276652703 0.0497382187250397],...
%         'Orientation','horizontal');
% %     saveas(gcf,strcat('graficos/png/',grid,'_x_',grid,'energyconsumed.png'));
% %     saveas(gcf,'graficos/pdf/energyconsumed.pdf');
% %     saveas(gcf,'graficos/eps/energyconsumed.eps', 'epsc');
% 
% end