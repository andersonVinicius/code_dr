
% path35 = '30_x_30_35000_cenario_6.mat';
% % success_rate35 = success_rate(path35) 
% path1_20 = '30_x_30_20000_cenario_6.mat';
% 
% paths = success_rate_all(path1_20);
% paths(length(paths)+1,:) = success_rate(path35);
load('success_rate.mat')
ymatrix1 = paths

% Create figure
figure1 = figure;
colormap(jet);

% Create axes
axes1 = axes('Parent',figure1);
hold(axes1,'on');

% Create multiple lines using matrix input to bar
bar1 = bar(ymatrix1,'BarWidth',1,'Parent',axes1);
set(bar1(1),'DisplayName','Q-learning egreedy WO ',...
    'FaceColor',[0.756862759590149 0.866666674613953 0.776470601558685]);
set(bar1(2),'DisplayName','Simple Q-learning WO',...
    'FaceColor',[0.584313750267029 0.388235300779343 0.388235300779343]);
set(bar1(3),'DisplayName','Sarsa WO',...
    'FaceColor',[0.952941179275513 0.87058824300766 0.733333349227905]);

% Create ylabel
ylabel('Success rate (%)','HorizontalAlignment','center','FontSize',12);

% Create xlabel
xlabel('Episodes ','HorizontalAlignment','center','FontSize',12);

box(axes1,'on');
% Set the remaining axes properties
set(axes1,'XGrid','on','XMinorTick','on','XTick',[1 2 3 4 5 6 7 8],...
    'XTickLabel',{'1000','3000','5000','7000','10000','15000','20000','25000'},...
    'YGrid','on');
% Create legend
legend1 = legend(axes1,'show');
set(legend1,...
    'Position',[0.178528350766216 0.744144144144144 0.148648430236422 0.144455574809965]);



function sr = success_rate(data_set)

    load(data_set);
    data_egreedy = table2array(egreedy(:,6));
    data_simpleql = table2array(simpleQl(:,6));
    data_sarsa = table2array(sarsa(:, 6));

    cont_egreedy = 0;
    cont_simpleql = 0;
    cont_sarsa = 0;
    for i =1:length(data_egreedy)

        if data_egreedy(i) == 'False'
            cont_egreedy = cont_egreedy + 1;
        end

        if data_simpleql(i) == 'False'
            cont_simpleql = cont_simpleql + 1;
        end

        if data_sarsa(i) == 'False'
            cont_sarsa = cont_sarsa + 1;
        end

    end

    sr = [cont_egreedy, cont_simpleql, cont_sarsa]/length(data_egreedy) * 100;

end


function sr = success_rate_all(data_set)
   
    load(data_set);   
    eps = unique(egreedy.num_episodes);
    
    for j = 1:length(eps)
        
        data_egreedy = table2array(egreedy(find(egreedy.num_episodes == eps(j)),6));
        data_simpleql = table2array(simpleQl(find(simpleQl.num_episodes == eps(j)),6));
        data_sarsa = table2array(sarsa(find(sarsa.num_episodes == eps(j)),6));

        cont_egreedy = 0;
        cont_simpleql = 0;
        cont_sarsa = 0;
        for i =1:length(data_egreedy)

            if data_egreedy(i) == 'False'
                cont_egreedy = cont_egreedy + 1;
            end

            if data_simpleql(i) == 'False'
                cont_simpleql = cont_simpleql + 1;
            end

            if data_sarsa(i) == 'False'
                cont_sarsa = cont_sarsa + 1;
            end

        end

        sr(j,:) = [cont_egreedy, cont_simpleql, cont_sarsa]/length(data_egreedy) * 100;
      
    end
end


