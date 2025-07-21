'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.isinf\ntorch.isinf(input)\n'
import torch
input = torch.tensor([1.0, (- 1.0), float('inf'), float('-inf'), float('nan')])
print(torch.isinf(input))