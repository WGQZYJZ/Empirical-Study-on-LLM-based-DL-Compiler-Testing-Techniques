'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.set_num_threads\ntorch.set_num_threads(int)\n'
import torch
input_data = torch.rand(1000000)
torch.set_num_threads(1)
result = torch.sum(input_data)
print(result)