'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.special.exp2\ntorch.special.exp2(input, *, out=None)\n'
import torch
print('Task 1: import PyTorch')
print('Task 2: Generate input data')
input_data = torch.rand(5, 5)
print(input_data)
print('Task 3: Call the API torch.special.exp2')
output_data = torch.special.exp2(input_data)
print(output_data)
print('Task 4: Call the API torch.special.exp2 with out')
output_data = torch.rand(5, 5)
torch.special.exp2(input_data, out=output_data)
print(output_data)