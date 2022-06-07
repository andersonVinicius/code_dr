
config_grid = {'5','10','15', '20', '30'} 
eleito = 1;

path_naive = 'data_naive/5_consumerEnergyUavForMissionQLeNaive.csv';
path_naive2 = 'data_naive/10_consumerEnergyUavForMissionQLeNaive.csv';
path_naive3 = 'data_naive/15_consumerEnergyUavForMissionQLeNaive.csv';
path_naive4 = 'data_naive/20_consumerEnergyUavForMissionQLeNaive.csv';

% path_naive = strcat('data_naive/',config_grid{eleito},'_consumerEnergyUavForMissionQLeNaive.csv');
% path_sarsa = strcat('data_sarsa/',config_grid{eleito},'_x_',config_grid{eleito},'consumerEnergyUavForMissionQLeSarsa.csv');
% path_egreedy = strcat('data_egreedy/',config_grid{eleito},'_x_',config_grid{eleito},'_consumerEnergyUavForMissionQLe.csv');
% path_simple_ql = strcat('data_simple_ql/',config_grid{eleito},'_x_',config_grid{eleito},'_consumerEnergyUavForMissionQLeSarsa.csv');

% 
% paths = {path_naive, path_sarsa, ...
%          path_egreedy, path_simple_ql
%          };
paths = {path_naive, path_naive2, path_naive3, path_naive4}

for path_id = 1:length(paths) 
    data = readtable(paths{path_id});
    mat_energy(path_id,:) = table2array(data(1,1:15));
end    
 %call barPlot
 building_bar_energy(mat_energy, config_grid{1})


function [] = building_bar_energy(mat_energy, grid)

    % Create figure
    figure1 = figure;

    % Create axes
    axes1 = axes('Parent',figure1,...
    'Position',[0.11449016100179 0.11 0.829338103756708 0.727696335078534]);
hold(axes1,'on');

    bar1 = bar(mat_energy');

    set(bar1(4),'DisplayName','Simple Q-learning',...
        'FaceColor',[0.39215686917305 0.474509805440903 0.635294139385223]);
    set(bar1(3),'DisplayName','Egreedy Q-learning',...
        'FaceColor',[0.529411792755127 0.317647069692612 0.317647069692612]);
    set(bar1(2),'DisplayName','Sarsa',...
        'FaceColor',[0.756862759590149 0.866666674613953 0.776470601558685]);
    set(bar1(1),'DisplayName','naive',...
        'FaceColor',[0.952941179275513 0.87058824300766 0.733333349227905]);

    % Create ylabel
    ylabel('Energy consumed(j)');

    % Create xlabel
    xlabel('ID UAV');

    box(axes1,'on');
    % Set the remaining axes properties
    set(axes1,'XTick',[1 2 3 4 5 6 7 8 9 10 11 12 13 14 15],'XTickLabel',...
        {'1','2','3','4','5','6','7','8','9','10','11','12','13','14','15'},'YGrid',...
        'on');
    % Create legend
    legend1 = legend(axes1,'show');
    set(legend1,...
        'Position',[0.284287393325817 0.885034906939582 0.435599276652703 0.0497382187250397],...
        'Orientation','horizontal');
    saveas(gcf,strcat('graficos/png/',grid,'_x_',grid,'energyconsumed.png'));
    saveas(gcf,'graficos/pdf/energyconsumed.pdf');
    saveas(gcf,'graficos/eps/energyconsumed.eps', 'epsc');

end

