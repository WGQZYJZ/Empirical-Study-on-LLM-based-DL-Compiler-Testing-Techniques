'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.isinf\ntorch.isinf(input)\n'
import torch
input_data = torch.rand(4, 4)
print(torch.isinf(input_data))
input_data = torch.tensor([1, float('inf'), float('-inf'), float('nan')])
print(torch.isinf(input_data))