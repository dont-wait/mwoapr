from mWOAPR import mWOAPR
def main():
    pop_size = 500
    function_name = 'F10'
    max_iterater = 100
    mwoapr = mWOAPR(pop_size, function_name, max_iterater)
    best_solution, best_fitness = mwoapr.mWOAPR_handle()
    print("Giải pháp tốt nhất:", best_solution, best_fitness)
main()