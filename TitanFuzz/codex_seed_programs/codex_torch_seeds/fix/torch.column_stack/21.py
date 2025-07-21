'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.column_stack\ntorch.column_stack(tensors, *, out=None)\n'
import torch
import torch
input_tensor_1 = torch.randn(2, 3)
print('input_tensor_1: ', input_tensor_1)
input_tensor_2 = torch.randn(2, 3)
print('input_tensor_2: ', input_tensor_2)
output_tensor = torch.column_stack((input_tensor_1, input_tensor_2))
print('output_tensor: ', output_tensor)