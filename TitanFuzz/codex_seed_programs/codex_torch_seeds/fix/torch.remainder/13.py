'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.remainder\ntorch.remainder(input, other, *, out=None)\n'
import torch
input_data = torch.randint(10, (3, 3), dtype=torch.float64)
print(input_data)
input_data = torch.randint(10, (3, 3), dtype=torch.float64)
print(input_data)
output = torch.remainder(input_data, 2)
print(output)