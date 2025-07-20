import os

error_keywords = [
    "BothExecFail",
    "ExecStateCatch",
    "ExceptMsgCatch",
    "GpuExecFail",
    "VarInconsistentCatch",
    "InternalRandomFail",
    "GpuNotImplementedFail",
    "ComparisonFail",
    "TimeoutFail",
    "RandCheckExecFail"
]

error_folder = 'error'
if not os.path.exists(error_folder):
    os.makedirs(error_folder)

with open('trace.txt', 'r', encoding='latin-1') as trace_file:
    output_files = {keyword: open(os.path.join(error_folder, f'{keyword}.txt'), 'w') for keyword in error_keywords}
    
    for line in trace_file:
        for keyword in error_keywords:
            if keyword in line:
                output_files[keyword].write(line)
    
    for file in output_files.values():
        file.close()

print(f"Success!")