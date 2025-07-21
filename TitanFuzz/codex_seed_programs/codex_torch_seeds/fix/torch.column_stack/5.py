'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.column_stack\ntorch.column_stack(tensors, *, out=None)\n'
import torch
input_data = [torch.rand(1, 2), torch.rand(1, 2)]
print('Input:', input_data)
output_data = torch.column_stack(input_data)
print('Output:', output_data)