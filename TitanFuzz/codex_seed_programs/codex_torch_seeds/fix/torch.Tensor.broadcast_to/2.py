'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.broadcast_to\ntorch.Tensor.broadcast_to(_input_tensor, shape)\n'
import torch
input_tensor = torch.randn(1, 3)
output_tensor = torch.Tensor.broadcast_to(input_tensor, (3, 3))
print(output_tensor)