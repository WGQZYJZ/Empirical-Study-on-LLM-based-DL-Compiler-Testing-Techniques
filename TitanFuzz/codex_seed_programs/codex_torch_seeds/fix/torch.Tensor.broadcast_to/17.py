'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.broadcast_to\ntorch.Tensor.broadcast_to(_input_tensor, shape)\n'
import torch
input_tensor = torch.arange(6)
input_tensor = input_tensor.view(2, 3)
print(input_tensor)
output_tensor = input_tensor.broadcast_to(shape=(2, 3, 3))
print(output_tensor)