
g = 10;% m/s^2
m=90; %kg
vUav=15;% m/s 
energy = zeros(1,15);
energyN = zeros(1,15);

for i=1:15
    
%     enegyQL(i) = (  (m * ( (vUav + pontoDePartidaUavWindSpeed(i)) ^2)* pontoDePartidaUavNewDistace(i)) + (m * g * pontoDePartidaUavNewDistace(i)) )/ (2*vUav);
    
    enegyN(i) = (  (m * ( (vUav + 13.1)^2)* pontoDePartidaUavOldDistace(i)*1000) + (m * g * pontoDePartidaUavOldDistace(i)*1000) )/ (2*vUav);
    enegyNWW(i) = (  (m * ( (vUav)^2)* pontoDePartidaUavOldDistace(i)*1000) + (m * g * pontoDePartidaUavOldDistace(i)*1000) )/ (2*vUav);
    
end    