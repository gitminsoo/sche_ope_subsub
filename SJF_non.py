import json
import json_parse
import draw_Gantt

def SJF_non(process):
    
    pro_num = len(process)
    
    left_time = [0] * pro_num
    
    run_idx = -1
    
    running_time = 0
    
    res = [-1]*pro_num
    
    term = [0]*pro_num
    
    f_check = 0
    
    for i in range(0,pro_num):
       
        left_time[i] = process[i]['burst_time']
        
    idx_ret = list()    
    
    ret = list()
    
    min = 0
    
    while(True):
        
        for i in range(0,pro_num):
            f_check = f_check + left_time[i]
        
        if(f_check == 0):
            break
        f_check = 0
        
        if(run_idx < 0):
            for i in range(0,pro_num):
                if(process[min]['burst_time']>process[i]['burst_time']):
                    min = i
            run_idx = min
        
        if(left_time[run_idx] == 0):
            for i in range(0,pro_num):
                if(left_time[i]>0):
                    min = i
            for i in range(0,pro_num):
                if(left_time[i]>0):
                    if(process[min]['burst_time']>process[i]['burst_time']):
                        min = i
            run_idx = min
        
        print(run_idx)
        
        
        
        idx_ret.append(run_idx)
        running_time = running_time + 1 
        left_time[run_idx] = left_time[run_idx] - 1
        
    
            
    
    ret.append(idx_ret)
    
    return ret
     
           
    
    
    
    
    
    
with open('./process_SJF_non.json','r') as f:
    data = json.load(f)

process = json_parse.make_process(data)
pre = json_parse.extract_preemptive(data)

ret = SJF_non(process)

draw_Gantt.draw_schedule(ret[0])