'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.broadcast_to\ntorch.Tensor.broadcast_to(_input_tensor, shape)\n'
import torch
'\nTask 1: import PyTorch\n'
'\nTask 2: Generate input data\n'
input_tensor = torch.arange(12, dtype=torch.float32).reshape(3, 4)
'\nTask 3: Call the API torch.Tensor.broadcast_to\ntorch.Tensor.broadcast_to(_input_tensor, shape)\n'
output_tensor = torch.Tensor.broadcast_to(input_tensor, (2, 3, 4))
print('The input tensor is:', input_tensor)
print('The output tensor is:', output_tensor)