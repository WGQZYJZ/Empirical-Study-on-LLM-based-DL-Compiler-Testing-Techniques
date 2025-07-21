'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.isinf\ntorch.isinf(input)\n'
import torch
input_data = torch.tensor([1, 2, 3, float('inf'), float('-inf')])
print(input_data)
print(torch.isinf(input_data))