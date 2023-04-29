import json

import json_parse

import draw_Gantt

def Priority_pre(process) :
    
    print(process)
    
    # num of process
    pro_num = len(process)
    
    # total time
    running_time = 0
    
    # each process's left time
    left_time = [0] * pro_num
    
    for i in range(0,pro_num):
        left_time[i] = process[i]['burst_time']
    
    # running state's idx
    run_idx = -1
    
    # response time array
    res = [-1] * pro_num
    
    # terminate time
    term = [0] * pro_num
    
    f_check = 0
    
    hi_pri = -1
    
    idx_ret = list()
    
    ret = list()
    
    while(True):
        
        # 실행하던 프로세스가 끝나서 스케쥴링 하는 경우
        if(left_time[run_idx]==0):
           hi_pri = -1
           for i in range(0,pro_num):
               if(process[i]['arrival_time']<=running_time):
                   if(left_time[i]>0):
                    if(hi_pri == -1 or process[i]['priority']<process[hi_pri]['priority']):
                       hi_pri = i
               
           run_idx = hi_pri
        
        # 새로운 프로세스가 들어와 스케쥴링 하는 경우
        for i in range(0,pro_num):
            if(process[i]['arrival_time'] == running_time):
                if(run_idx == -1):
                    run_idx = i
                else:
                    if(process[run_idx]['priority'] > process[i]['priority']):
                        run_idx = i
            
        
        idx_ret.append(run_idx)
        left_time[run_idx] = left_time[run_idx] - 1
        running_time = running_time +1
        
        for i in range(0,pro_num):
            f_check = f_check + left_time[i]
        
        if(f_check == 0):
            term[run_idx] = running_time
            break
        f_check = 0
    
    ret.append(idx_ret)
    
    return ret
                        
                
                    
        
             
            
    

    
        
        

with open('./process_Priority_pre.json','r') as f:
    data = json.load(f)

process = json_parse.make_process(data)

ret = Priority_pre(process)
    
draw_Gantt.draw_schedule(ret[0])