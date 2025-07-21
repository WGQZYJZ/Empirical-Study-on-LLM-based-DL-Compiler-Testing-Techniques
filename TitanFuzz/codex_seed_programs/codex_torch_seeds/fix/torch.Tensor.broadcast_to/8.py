'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.broadcast_to\ntorch.Tensor.broadcast_to(_input_tensor, shape)\n'
import torch
input_data = torch.Tensor([1, 2, 3])
output_data = input_data.broadcast_to(shape=(3, 3))
print(output_data)