'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.broadcast_to\ntorch.Tensor.broadcast_to(_input_tensor, shape)\n'
import torch
import torch
input_tensor = torch.rand(1, 3, 1, 1)
output_tensor = torch.Tensor.broadcast_to(input_tensor, (2, 3, 4, 5))
print(output_tensor)
'\ntorch.Size([2, 3, 4, 5])\n'