'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.ndimension\ntorch.Tensor.ndimension(_input_tensor)\n'
import torch
_input_tensor = torch.randn(2, 3)
print("Input tensor's dimension: {}".format(_input_tensor.ndimension()))
print("Input tensor's shape: {}".format(_input_tensor.shape))
print("Input tensor's size: {}".format(_input_tensor.size()))
print("Input tensor's numel: {}".format(_input_tensor.numel()))