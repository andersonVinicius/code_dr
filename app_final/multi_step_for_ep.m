id_grid = 1;
config_grid = {'30'};
scenario = {'1','2','3','4','5','6' };
vel_uav = 15;
for z = 1:6
    sarsa = strcat('data_sarsa/',config_grid{id_grid},'_x_',config_grid{id_grid},'_delta_for_ep_scn',scenario{z},'.csv');
    egreedy = strcat('data_egreedy/',config_grid{id_grid},'_x_',config_grid{id_grid},'_delta_for_ep_scn',scenario{z},'.csv');
    simple_ql = strcat('data_simple_ql/',config_grid{id_grid},'_x_',config_grid{id_grid},'_delta_for_ep_scn',scenario{z},'.csv');

    
    aux_mean_1000_delta_simpleQL = [];
    aux_mean_1000_delta_egreedy = [];
    aux_mean_1000_delta_sarsa = [];
  
%     range = 500
%     limit_ary = 10000
    switch (z)
        case 1
            range = 1000;
            limit_ary = 25000;
            
            data_simple_ql = readtable(simple_ql);
            simple_ql_arr_num = (table2array(data_simple_ql(1:limit_ary, 1)) + 30) * vel_uav ;
            
            data_egreedy = readtable(egreedy);
            egreedy_arr_num = (table2array(data_egreedy(1:limit_ary, 1))+ 30) * vel_uav ;
            
            data_sarsa = readtable(sarsa);
            sarsa_arr_num = (table2array(data_sarsa(1:limit_ary, 1)) + 30) * vel_uav ;
           
        case 2
            range = 1000;
            limit_ary = 25000;
            data_simple_ql = readtable(simple_ql);
            simple_ql_arr_num = (table2array(data_simple_ql(1:limit_ary, 1)) + 30) * vel_uav ;
            
            data_egreedy = readtable(egreedy);
            egreedy_arr_num = (table2array(data_egreedy(1:limit_ary, 1)) + 30) * vel_uav ;
            
            data_sarsa = readtable(sarsa);
            sarsa_arr_num = (table2array(data_sarsa(1:limit_ary, 1)) + 30) * vel_uav ;
        case 3
            range = 1000;
            limit_ary = 25000;
            
            data_simple_ql = readtable(simple_ql);
            simple_ql_arr_num = (table2array(data_simple_ql(1:limit_ary, 1)) + 30) * vel_uav ;
            
            data_egreedy = readtable(egreedy);
            egreedy_arr_num = (table2array(data_egreedy(1:limit_ary, 1)) + 30) * vel_uav ;
            
            data_sarsa = readtable(sarsa);
            sarsa_arr_num = (table2array(data_sarsa(1:limit_ary, 1)) + 30) * vel_uav ;
        case 4
            range = 1000;
            limit_ary = 25000;
            data_simple_ql = readtable(simple_ql);
            simple_ql_arr_num = (table2array(data_simple_ql(1:limit_ary, 1))+ 30) * vel_uav ;
            
            data_egreedy = readtable(egreedy);
            egreedy_arr_num = (table2array(data_egreedy(1:limit_ary, 1))+ 30) * vel_uav ;
            
            data_sarsa = readtable(sarsa);
            sarsa_arr_num = (table2array(data_sarsa(1:limit_ary, 1))+ 30) * vel_uav ;
        case 5
            range = 1000;
            limit_ary = 50000;
            data_simple_ql = readtable(simple_ql);
            simple_ql_arr_num = (table2array(data_simple_ql(1:limit_ary, 1))+ 30) * vel_uav ;
            
            data_egreedy = readtable(egreedy);
            egreedy_arr_num = (table2array(data_egreedy(1:limit_ary, 1))+ 30) * vel_uav ;
            
            data_sarsa = readtable(sarsa);
            sarsa_arr_num = (table2array(data_sarsa(1:limit_ary, 1))+ 30) * vel_uav ;
        otherwise
            range = 1000;
            limit_ary = 50000;
            data_simple_ql = readtable(simple_ql);
            simple_ql_arr_num = (table2array(data_simple_ql(1:limit_ary, 1))+ 30)* vel_uav ;
            
            data_egreedy = readtable(egreedy);
            egreedy_arr_num = (table2array(data_egreedy(1:limit_ary, 1))+ 30)* vel_uav ;
            
            data_sarsa = readtable(sarsa);
            sarsa_arr_num = (table2array(data_sarsa(1:limit_ary, 1))+ 30) * vel_uav ;
    end
    
    j = 1;
    
    for i = 1:range:(limit_ary-range)

       aux_mean_1000_delta_simpleQL(j) = mean(simple_ql_arr_num (i:i+range) ) ;
       aux_mean_1000_delta_egreedy(j) = mean(egreedy_arr_num(i:i+range) )  ;
       aux_mean_1000_delta_sarsa(j) = mean(sarsa_arr_num(i:i+range))  ;
       j=j+1;      
    end

    % % Create figure
    % figure1 = figure;
    % 
    % % Create axes
    % axes1 = axes('Parent',figure1);
    % hold(axes1,'on');
    subplot (3,2,z)

    plot(aux_mean_1000_delta_simpleQL,'DisplayName','Simple Q-learning','Marker','o','LineWidth',2);
    hold on
    plot(aux_mean_1000_delta_egreedy,'DisplayName','Q-learning Egreedy','Marker','hexagram','LineWidth',2);
    hold on
    plot(aux_mean_1000_delta_sarsa,'DisplayName','Sarsa','Marker','pentagram','LineWidth',2);

    % Create ylabel
    ylabel('Distance (meters)');

    % Create xlabel
    xlabel('Episodes');

    title(strcat('Scenario[',scenario{z},']'));

end





% subplot (3,2,2)
% 
% plot(aux_mean_1000_delta_simpleQL,'DisplayName','Simple Q-learning','Marker','o','LineWidth',2);
% hold on
% plot(aux_mean_1000_delta_egreedy,'DisplayName','Q-learning Egreedy','Marker','hexagram','LineWidth',2);
% hold on
% plot(aux_mean_1000_delta_sarsa,'DisplayName','Sarsa','Marker','pentagram','LineWidth',2);
% 
% % Create ylabel
% ylabel('Distance (meters)');
% 
% % Create xlabel
% xlabel('Episodes');
% title('Scenario 2')
% 
% 
% subplot (3,2,3)
% 
% 
% plot(aux_mean_1000_delta_simpleQL,'DisplayName','Simple Q-learning','Marker','o','LineWidth',2);
% hold on
% plot(aux_mean_1000_delta_egreedy,'DisplayName','Q-learning Egreedy','Marker','hexagram','LineWidth',2);
% hold on
% plot(aux_mean_1000_delta_sarsa,'DisplayName','Sarsa','Marker','pentagram','LineWidth',2);
% 
% % Create ylabel
% ylabel('Distance (meters)');
% 
% % Create xlabel
% xlabel('Episodes');
% 
% title('Scenario 3')
% 
% subplot (3,2,4)
% 
% 
% plot(aux_mean_1000_delta_simpleQL,'DisplayName','Simple Q-learning','Marker','o','LineWidth',2);
% hold on
% plot(aux_mean_1000_delta_egreedy,'DisplayName','Q-learning Egreedy','Marker','hexagram','LineWidth',2);
% hold on
% plot(aux_mean_1000_delta_sarsa,'DisplayName','Sarsa','Marker','pentagram','LineWidth',2);
% 
% % Create ylabel
% ylabel('Distance (meters)');
% 
% % Create xlabel
% xlabel('Episodes');
% 
% title('Scenario 4')
% 
% subplot (3,2,5)
% 
% 
% plot(aux_mean_1000_delta_simpleQL,'DisplayName','Simple Q-learning','Marker','o','LineWidth',2);
% hold on
% plot(aux_mean_1000_delta_egreedy,'DisplayName','Q-learning Egreedy','Marker','hexagram','LineWidth',2);
% hold on
% plot(aux_mean_1000_delta_sarsa,'DisplayName','Sarsa','Marker','pentagram','LineWidth',2);
% 
% % Create ylabel
% ylabel('Distance (meters)');
% 
% % Create xlabel
% xlabel('Episodes');
% title('Scenario 5')
% 
% % box(axes1,'on');
% % grid(axes1,'on');
% 
% % % Set the remaining axes properties
% % set(axes1,'XMinorTick','on','XTickLabel',...
% %     {'0','5000','10000','15000','20000','25000','30000','35000','40000','45000','50000'});
% % % Create legend
% % legend(axes1,'show');
% 
