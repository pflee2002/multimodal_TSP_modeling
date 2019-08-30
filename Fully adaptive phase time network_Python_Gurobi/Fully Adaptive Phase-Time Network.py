from gurobipy import *

n_start_phase = 1
n_start_time = 1
n_end_phase = 9
n_end_time = 121
n_total_phase = 9
n_total_time = 121
n_total_TSP = 13
# =============================================================================
# Defineing Global Variables
# =============================================================================
links_tsp1 = list()   # arcs served in TSP 1
links_tsp2 = list()   # arcs served in TSP 2
links_tsp3 = list()   # arcs served in TSP 3 
links_tsp4 = list()   # arcs served in TSP 4
links_tsp5 = list()   # arcs served in TSP 5
links_tsp6 = list()   # arcs served in TSP 6
links_tsp7 = list()   # arcs served in TSP 7 
links_tsp8 = list()   # arcs served in TSP 8
links_tsp9 = list()   # arcs served in TSP 9
links_tsp10 = list()  # arcs served in TSP 10
links_tsp11 = list()  # arcs served in TSP 11
links_tsp12 = list()  # arcs served in TSP 12
links_tsp13 = list()  # arcs served in TSP 13
links_clone5 = list() # arcs served by clone phase 5
links_clone6 = list() # arcs served by clone phase 6
links_clone7 = list() # arcs served by clone phase 7
links_clone8 = list() # arcs served by clone phase 8
links = list()        # phase time network arcs

all_tsp = list() #placeing all TSP into one single list
cost = {}
droped_tsp_list = list() #a list for the TSP dropped during iteration
all_clone = [5,6,7,8] #5 represents clone phase 1,6 represents clone phase 2,7 represents clone phase 3,8 represents clone phase 4
# =============================================================================
# Reading the first input file
# =============================================================================
f = open("phase_time_network.txt", "r")
line = f.readline()
counter = 0 
while(len(line)):
    line = line.strip('\n')
    data = line.split()
    start_phase = int(data[0])
    start_time = int(data[1])
    end_phase = int(data[2])
    end_time = int(data[3])
    tsp_1 = int(data[4])
    tsp_2 = int(data[5])
    tsp_3 = int(data[6])
    tsp_4 = int(data[7])
    tsp_5 = int(data[8])
    tsp_6 = int(data[9])
    tsp_7 = int(data[10])
    tsp_8 = int(data[11])
    tsp_9 = int(data[12])
    tsp_10 = int(data[13])
    tsp_11 = int(data[14])
    tsp_12 = int(data[15])
    tsp_13 = int(data[16])  
    clone_5 = int(data[17]) 
    clone_6 = int(data[18])
    clone_7 = int(data[19]) 
    clone_8 = int(data[20])
    links.append((start_phase,start_time,end_phase,end_time))
# =============================================================================
# Adding all TSP request into one list
# =============================================================================
    counter=0
    if(tsp_1>0):
        counter=counter+1
        links_tsp1.append((start_phase,start_time,end_phase,end_time))      
        if 1 not in all_tsp:
            all_tsp.append(1)
        
    if (tsp_2>0):
        counter=counter+1
        links_tsp2.append((start_phase,start_time,end_phase,end_time))
        if 2 not in all_tsp:
            all_tsp.append(2)
            
    if(tsp_3>0):
        counter=counter+1
        links_tsp3.append((start_phase,start_time,end_phase,end_time))
        if 3 not in all_tsp:
            all_tsp.append(3)
       
    if (tsp_4>0):
        counter=counter+1
        links_tsp4.append((start_phase,start_time,end_phase,end_time))
        if 4 not in all_tsp:
            all_tsp.append(4)
        
    if(tsp_5>0):
        counter=counter+1
        links_tsp5.append((start_phase,start_time,end_phase,end_time))
        if 5 not in all_tsp:
            all_tsp.append(5)

    if (tsp_6>0):
        counter=counter+1
        links_tsp6.append((start_phase,start_time,end_phase,end_time))
        if 6 not in all_tsp:
            all_tsp.append(6)

    if(tsp_7>0):
        counter=counter+1
        links_tsp7.append((start_phase,start_time,end_phase,end_time))
        if 7 not in all_tsp:
            all_tsp.append(7)

    if (tsp_8>0):
        counter=counter+1
        links_tsp8.append((start_phase,start_time,end_phase,end_time))
        if 8 not in all_tsp:
            all_tsp.append(8)

    if(tsp_9>0):
        counter=counter+1
        links_tsp9.append((start_phase,start_time,end_phase,end_time))
        if 9 not in all_tsp:
            all_tsp.append(9)
         
    if (tsp_10>0):
        counter=counter+1
        links_tsp10.append((start_phase,start_time,end_phase,end_time))
        if 10 not in all_tsp:
            all_tsp.append(10)

    if(tsp_11>0):
        counter=counter+1
        links_tsp11.append((start_phase,start_time,end_phase,end_time))
        if 11 not in all_tsp:
            all_tsp.append(11)
       
    if (tsp_12>0):
        counter=counter+1
        links_tsp12.append((start_phase,start_time,end_phase,end_time))
        if 12 not in all_tsp:
            all_tsp.append(12)

    if (tsp_13>0):
        counter=counter+1
        links_tsp13.append((start_phase,start_time,end_phase,end_time))
        if 13 not in all_tsp:
            all_tsp.append(13)
 
    if(counter>0):
        cost[(start_phase,start_time,end_phase,end_time)]=counter*(-100)    
    else:
        cost[(start_phase,start_time,end_phase,end_time)]=1    
    line = f.readline()
f.close() 

# =============================================================================
# Mapping TSP arc information into a Dictionary 
# =============================================================================
tsp_no_to_tsp_links_map=dict();
tsp_no_to_tsp_links_map[1]=links_tsp1;
tsp_no_to_tsp_links_map[2]=links_tsp2;
tsp_no_to_tsp_links_map[3]=links_tsp3;
tsp_no_to_tsp_links_map[4]=links_tsp4;
tsp_no_to_tsp_links_map[5]=links_tsp5;
tsp_no_to_tsp_links_map[6]=links_tsp6;
tsp_no_to_tsp_links_map[7]=links_tsp7;
tsp_no_to_tsp_links_map[8]=links_tsp8;
tsp_no_to_tsp_links_map[9]=links_tsp9;
tsp_no_to_tsp_links_map[10]=links_tsp10;
tsp_no_to_tsp_links_map[11]=links_tsp11;
tsp_no_to_tsp_links_map[12]=links_tsp12;
tsp_no_to_tsp_links_map[13]=links_tsp13;
tsp2clone_phase_map=dict();
tsp2clone_phase_map[1]=5;
tsp2clone_phase_map[2]=7;
tsp2clone_phase_map[3]=5;
tsp2clone_phase_map[4]=6;
tsp2clone_phase_map[5]=8;
tsp2clone_phase_map[6]=5;
tsp2clone_phase_map[7]=7;
tsp2clone_phase_map[8]=8;
tsp2clone_phase_map[9]=7;
tsp2clone_phase_map[10]=6;
tsp2clone_phase_map[11]=5;
tsp2clone_phase_map[12]=5;
tsp2clone_phase_map[13]=7; 
# =============================================================================
# Mapping all high tsp and all low tsp into separate lists
# =============================================================================
high_tsp = list()
if 1 not in high_tsp:
    high_tsp.append(1)
if 2 not in high_tsp:
    high_tsp.append(2)
if 6 not in high_tsp:
    high_tsp.append(6)
if 10 not in high_tsp:
    high_tsp.append(10)    
if 11 not in high_tsp:
    high_tsp.append(11)
if 12 not in high_tsp:
    high_tsp.append(12)
if 13 not in high_tsp:
    high_tsp.append(13)


low_tsp = list()
if 8 not in low_tsp:
    low_tsp.append(8)
if 7 not in low_tsp:
    low_tsp.append(7)
if 3 not in low_tsp:
    low_tsp.append(3)
if 4 not in low_tsp:
    low_tsp.append(4)    
if 5 not in low_tsp:
    low_tsp.append(5)
if 9 not in low_tsp:
    low_tsp.append(9)
# =============================================================================
# Reading the second input file for clone arcs
# =============================================================================
c1 = open("clone_phase_1.txt", "r")
line = c1.readline()
counter_1 = 0  #for clone arcs
while(len(line)):
    line = line.strip('\n')
    data = line.split()
    start_phase = int(data[0])
    start_time = int(data[1])
    end_phase = int(data[2])
    end_time = int(data[3]) 
    clone_5 = int(data[17]) 

    counter_1=0    
    if (clone_5>0):
        counter_1=counter_1+1
        links_clone5.append((start_phase,start_time,end_phase,end_time))     
    if(counter_1>0):
        cost[(start_phase,start_time,end_phase,end_time)]=counter_1*(1000)
    else:
        cost[(start_phase,start_time,end_phase,end_time)]=1    
    line = c1.readline()
c1.close() 

c2 = open("clone_phase_2.txt", "r")
line = c2.readline()
counter_2 = 0  #for clone arcs
while(len(line)):
    line = line.strip('\n')
    data = line.split()
    start_phase = int(data[0])
    start_time = int(data[1])
    end_phase = int(data[2])
    end_time = int(data[3])
    clone_6 = int(data[18])

    counter_2=0    
    if (clone_6>0):
        counter_2=counter_2+1
        links_clone6.append((start_phase,start_time,end_phase,end_time))     
    if(counter_2>0):
        cost[(start_phase,start_time,end_phase,end_time)]=counter_2*(1000)
    else:
        cost[(start_phase,start_time,end_phase,end_time)]=1   
    line = c2.readline()
c2.close() 

c3 = open("clone_phase_3.txt", "r")
line = c3.readline()
counter_3 = 0  #for clone arcs
while(len(line)):
    line = line.strip('\n')
    data = line.split()
    start_phase = int(data[0])
    start_time = int(data[1])
    end_phase = int(data[2])
    end_time = int(data[3])
    clone_7 = int(data[19]) 

    counter_3=0    
    if (clone_7>0):
        counter_3=counter_3+1
        links_clone7.append((start_phase,start_time,end_phase,end_time))    
    if(counter_3>0):
        cost[(start_phase,start_time,end_phase,end_time)]=counter_1*(1000)
    else:
        cost[(start_phase,start_time,end_phase,end_time)]=1    
    line = c3.readline()
c3.close() 

c4 = open("clone_phase_4.txt", "r")
line = c4.readline()
counter_4 = 0  #for clone arcs
while(len(line)):
    line = line.strip('\n')
    data = line.split()
    start_phase = int(data[0])
    start_time = int(data[1])
    end_phase = int(data[2])
    end_time = int(data[3])
    clone_8 = int(data[20])
    counter_4=0    
    if (clone_8>0):
        counter_4=counter_4+1
        links_clone8.append((start_phase,start_time,end_phase,end_time)) 
    
    if(counter_4>0):
        cost[(start_phase,start_time,end_phase,end_time)]=counter_2*(1000)
    else:
        cost[(start_phase,start_time,end_phase,end_time)]=1   
    line = c4.readline()
c4.close()
# =============================================================================
# Mapping clone arc information into Dictionary 
# ===========================================================================
tsp_no_to_clone_phase_links_map=dict();
tsp_no_to_clone_phase_links_map[5]=links_clone5;
tsp_no_to_clone_phase_links_map[6]=links_clone6;
tsp_no_to_clone_phase_links_map[7]=links_clone7;
tsp_no_to_clone_phase_links_map[8]=links_clone8;

def solver(all_tsp): 
    m = Model("TSP")       
    y = m.addVars(links,vtype=GRB.BINARY, name ="phase_time_arc" )      
    #object function in equation 14
    m.setObjective(sum([cost[i,t,j,s]*y[i,t,j,s] for (i,t,j,s) in links]),GRB.MINIMIZE)   
    #flow balance constraints in equation 10,11 and 12 
    for i in range(1,n_total_phase+1):
        for t in range(1,n_total_time+1):
            m.addConstr(sum([y[ii, tt, jj, ss] for (ii,tt,jj,ss) in links if ii==i and tt==t]) - sum([y[jj, ss, ii, tt]for (jj,ss,ii,tt) in links if ii==i and tt==t]) == 
                        (1 if i == n_start_phase and t == n_start_time else -1 if i == n_end_phase and t == n_end_time else 0))   
    for k in all_tsp:
        tsp_links=list();
        clone_links=list();
        tsp_links=tsp_no_to_tsp_links_map[k];
        clone_phase_no=tsp2clone_phase_map[k];
        clone_links=tsp_no_to_clone_phase_links_map[clone_phase_no];
        #Constraint for resilient phase time node in equation 15   
        m.addConstr(sum([y[i, t, j, s] for (i,t,j,s) in tsp_links]) + sum([y[i, t, j, s] for (i,t,j,s) in clone_links]) ==1) 
        
    m.optimize() 
    p= []     
    if m.status == GRB.Status.OPTIMAL:
        print('The final solution is:')
        for (i,t,j,s) in links:
            if(y[i,t,j,s].x > 0) :
                p.append(tuple([i, t, j, s]))
                print(i, t, j, s,y[i, t, j, s].x)
    else:
        print("\n\nno solution found")

    Feasible=True
    for i,t,j,s in p:
         for c in all_clone:
             if i== c or j ==c:
                 Feasible=False

    return Feasible
   
if __name__=='__main__':
    print('\n\nSearching Optimum Solution')
    f=solver(all_tsp)
    if f==False:
        print("Drop the Low TSP requests")
        f=solver(high_tsp)
        if f==True:
            for l in low_tsp:
                if low_tsp != [] :
                    added_low_tsp = low_tsp[0]
                    high_tsp.append(added_low_tsp)
                    del low_tsp[0]
                    f=solver(high_tsp)
                    if f==False:
                        droped_tsp = added_low_tsp
                        droped_tsp_list.append(droped_tsp)
                        del added_low_tsp
                        del high_tsp[-1]
                        f=solver(high_tsp)
                    else:
                        print("end")
                else:
                    print("all low tsp served")
                
    else:
        print("All served")
        
