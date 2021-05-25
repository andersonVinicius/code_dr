close all; clear all; clc;
velToDistace= zeros(90,4,40)
dis = [10,15,20,25]% velocidade m/s
for z=1:90 % payload 
    for i=1:4 % speed
        for j=1:40 % distance
            Cd = 0.54; 
            A = 1.2; 
            D = 1.2754; 
            b = 8.7; 
            va = dis(i)+12.32;
            battery = 8000;
            payload = z+1; 
            distance = 1000 * (j);
            p = (0.5 * Cd * A * D * ((va).^ 3)) + ((payload).^ 2)/ (D * (b .^ 2) * va);
            t = distance/va;

            velToDistace(z,i,j)=((((2*p)/1000)*t));
        end
    end
end 
cont=0
for z=1:90 % payload 
    for i=1:4 % speed
        for j=1:40 % distance
            cont=cont+1;
            payload(cont)= z;
            spd(cont) = dis(i);
            distanceKm(cont)=j;
            energyConsu(cont)=velToDistace(z,i,j);
        
        end
    end
end 
payload=[1:90]
spd=[1:4]
distanceKm=[1:40]



[x1,y1,z1] = meshgrid(spd,payload,distanceKm);
[x1,y1,z1,c1] = ndgrid(payload,spd,distanceKm,energyConsu)



