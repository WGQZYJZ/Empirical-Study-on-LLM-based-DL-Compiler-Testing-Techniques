'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.set_num_interop_threads\ntorch.set_num_interop_threads(int)\n'
import torch
import time
input_data = torch.rand(100, 100)
torch.set_num_interop_threads(1)
start = time.time()
result = torch.matmul(input_data, input_data)
end = time.time()
print('Time to complete the calculation: {}'.format((end - start)))