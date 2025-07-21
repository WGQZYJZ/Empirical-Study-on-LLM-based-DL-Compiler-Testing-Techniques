'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.broadcast_tensors\ntorch.broadcast_tensors(*tensors)\n'
import torch
input_tensor = torch.rand(1, 1, 4, 4)
print('input_tensor: ', input_tensor)
output_tensor = torch.broadcast_tensors(input_tensor, input_tensor)
print('output_tensor: ', output_tensor)