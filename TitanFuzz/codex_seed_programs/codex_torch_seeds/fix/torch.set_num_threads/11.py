'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.set_num_threads\ntorch.set_num_threads(int)\n'
import torch
import time
import torch
input_data = torch.randn(1000, 1000)
torch.set_num_threads(4)
start = time.time()
output_data = torch.mm(input_data, input_data)
print(output_data)
end = time.time()
print((end - start))