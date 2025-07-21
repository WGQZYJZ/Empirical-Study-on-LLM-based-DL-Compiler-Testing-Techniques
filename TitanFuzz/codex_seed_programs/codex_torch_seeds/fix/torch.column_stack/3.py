'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.column_stack\ntorch.column_stack(tensors, *, out=None)\n'
import torch
import torch
input_data = [torch.randn(2, 3), torch.randn(2, 3), torch.randn(2, 3)]
output_data = torch.column_stack(input_data)
print('output_data: ', output_data)