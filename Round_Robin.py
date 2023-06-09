import json
import json_parse
import draw_Gantt

def Round_Robin(process,quantum):
    
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
    
    # last time
    quantum_check = 0
    
    # finish check
    f_check = 0
    
    idx_ret = list()
    
    ret = list()
    
    while(True):
        
        for i in range(0,pro_num):
            f_check = f_check + left_time[i]
        
        if(f_check == 0):
            break
        f_check = 0
        
        if (run_idx == -1):
            run_idx = 0
            res[run_idx] = running_time
            
        print(run_idx)
        
        idx_ret.append(run_idx)        
        left_time[run_idx] = left_time[run_idx] - 1
        running_time = running_time+1
        quantum_check = quantum_check +1
        
        
        if(quantum_check % quantum == 0):
            quantum_check = 0
            for i in range(0,pro_num):
                if(left_time[(run_idx + i + 1)%pro_num]>0):
                    run_idx = (run_idx + i + 1)%pro_num
                    if(res[run_idx]==-1):
                        res[run_idx] = running_time
                    break
        
        if(left_time[run_idx]==0):
            quantum_check = 0
            term[run_idx] = running_time
            for i in range(0,pro_num):
                if(left_time[(run_idx + i + 1)%pro_num]>0):
                    run_idx = (run_idx + i + 1)%pro_num
                    if(res[run_idx]==-1):
                        res[run_idx] = running_time
                    break
        
    ret.append(idx_ret)
    return ret
        

    
    
    
with open('./process_RR.json','r') as f:
    data = json.load(f)

process = json_parse.make_process(data)
pre = json_parse.extract_preemptive(data)


ret = Round_Robin(process,20)

draw_Gantt.draw_schedule(ret[0])