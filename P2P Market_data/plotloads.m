clc;close all;clear all
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
set(groot,'defaultLineLineWidth',1.0)

PLOT='PV';  %'PV' , 'load'


x0=10.01;
y0=100.01;
width=680*0.8;
height=300*0.8;
g=figure;
set(gcf,'position',[x0,y0,width,height])
set(0,'defaultAxesFontName','Times New Roman');

switch PLOT
    case 'PV'
        %PV
        PV=[0,0,0,0,0.00428630952380952,0.154369395502646,0.372763558465608,0.591764489947090,0.736500473280423,0.827865411375661,0.872169460582010,0.883260172751323,0.869711021428571,0.835547247089947,0.769625188888889,0.646395421164021,0.442570644179894,0.231954201587302,0.0556354129629630,0,0,0,0,0]*4;

        plot(PV,LineWidth=2)
        xlim([1 max(size(PV))])
        xlabel 'Time [h]'
        ylabel 'P [kW]'

    case 'load'

        %load the mat file

        load("loads24house.mat");
        L=Electricity_Profile;
        L=[L L L(:,1:7)];
        LLL=sort(L(:,3),'descend');
        LL=sort(sum(L')','descend')'/1000;


        plot(LLL,LineWidth=2)
        xticks([20:20:100]*max(size(LL))/100)
        xticklabels({'20','40','60','80','100'})
        xlim([1 max(size(LL))])
        xlabel 'Time [%]'
        ylabel 'P [W]'
end
set(g,'Units','Inches');
pos = get(g,'Position');
set(g,'PaperPositionMode','Auto','PaperUnits','Inches','PaperSize',[pos(3), pos(4)])
%print(g,fullfile(pwd,'Figures',[filegname]),'-dpng')
print(g,fullfile(pwd,['PVout' ]),'-depsc','-r0')

