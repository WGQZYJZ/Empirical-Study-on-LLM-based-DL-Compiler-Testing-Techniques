'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.broadcast_to\ntorch.Tensor.broadcast_to(_input_tensor, shape)\n'
import torch
import torch
input_tensor = torch.tensor([1, 2, 3])
broadcast_tensor = input_tensor.broadcast_to([3, 3, 3])
print(broadcast_tensor)