import json

import json_parse

import draw_Gantt

def FCFS(process) :

    pro_num = len(process)
    
    left_time = [0] * pro_num
    
    run_idx = -1
    
    running_time = 0
    
    res = [-1]*pro_num
    
    term = [0]*pro_num
    
    for i in range(0,pro_num):
       
        left_time[i] = process[i]['burst_time']
    
    ret = list()
    idx_ret = list()
    
    while(True):
        
        if(run_idx < 0):
            run_idx = 0
            if(res[run_idx] == -1):
                res[run_idx] = running_time
        
        
        for i in range(0,pro_num):
            if(i == run_idx):
                left_time[i] = left_time[i] - 1

        idx_ret.append(run_idx)
        
        running_time = running_time + 1 
        
        if(left_time[run_idx] == 0):
            term[run_idx] = running_time
            
            if(run_idx == (pro_num-1)):
                break
            else:
                run_idx = run_idx + 1
                if(res[run_idx] == -1):
                    res[run_idx] = running_time
    

    
    print(idx_ret)
    print(running_time)
    
    ret.append(idx_ret)
    
    return ret
    

        

with open('./process_FCFS.json','r') as f:
    data = json.load(f)

process = json_parse.make_process(data)

ret = FCFS(process)


draw_Gantt.draw_schedule(ret[0])
