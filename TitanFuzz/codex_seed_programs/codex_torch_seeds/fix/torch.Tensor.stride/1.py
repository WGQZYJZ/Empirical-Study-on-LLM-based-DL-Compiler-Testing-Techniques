'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.stride\ntorch.Tensor.stride(_input_tensor, dim)\n'
import torch
import torch
input_tensor = torch.rand(3, 3)
stride = input_tensor.stride(0)
print('stride: ', stride)
'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.stride\ntorch.Tensor.stride(_input_tensor, dim)\n'
import torch
import torch
input_tensor = torch.rand(3, 3)
stride = input_tensor.stride(1)
print('stride: ', stride)