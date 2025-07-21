'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.isinf\ntorch.isinf(input)\n'
import torch
input_data = torch.tensor([(- float('inf')), (- 1.0), 0.0, 1.0, float('inf')])
print(torch.isinf(input_data))