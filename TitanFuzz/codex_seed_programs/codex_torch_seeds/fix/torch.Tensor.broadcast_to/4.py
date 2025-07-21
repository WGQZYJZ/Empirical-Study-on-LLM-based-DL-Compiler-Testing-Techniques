'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.broadcast_to\ntorch.Tensor.broadcast_to(_input_tensor, shape)\n'
import torch
input_tensor = torch.arange(1, 5)
print(input_tensor)
print(torch.Tensor.broadcast_to(input_tensor, (4, 4)))