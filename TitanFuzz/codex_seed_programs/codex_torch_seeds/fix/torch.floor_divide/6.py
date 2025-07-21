'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.floor_divide\ntorch.floor_divide(input, other, *, out=None)\n'
import torch
input_data = torch.randint(0, 10, (3, 3), dtype=torch.float32)
print('Input data:\n', input_data)
output = torch.floor_divide(input_data, 2)
print('Output:\n', output)