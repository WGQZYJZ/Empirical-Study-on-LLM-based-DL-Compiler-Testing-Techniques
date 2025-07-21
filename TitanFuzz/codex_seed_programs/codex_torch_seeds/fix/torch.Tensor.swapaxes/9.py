'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.swapaxes\ntorch.Tensor.swapaxes(_input_tensor, axis0, axis1)\n'
import torch
import torch
input_tensor = torch.Tensor([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(torch.Tensor.swapaxes(input_tensor, 0, 1))