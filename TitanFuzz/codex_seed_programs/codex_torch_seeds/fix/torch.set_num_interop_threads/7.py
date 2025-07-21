'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.set_num_interop_threads\ntorch.set_num_interop_threads(int)\n'
import torch
import time
input_data = torch.rand(size=(1000, 1000))
torch.set_num_interop_threads(4)
start_time = time.time()
output_data = torch.matmul(input_data, input_data)
duration = (time.time() - start_time)
print(('Time taken for inference: %.4f seconds' % duration))