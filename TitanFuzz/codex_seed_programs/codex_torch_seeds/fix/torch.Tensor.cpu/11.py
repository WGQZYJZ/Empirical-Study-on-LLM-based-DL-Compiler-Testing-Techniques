'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.cpu\ntorch.Tensor.cpu(_input_tensor, memory_format=torch.preserve_format)\n'
import torch
input_tensor = torch.rand(2, 3, 4, 5, 6)
cpu_tensor = input_tensor.cpu()
print('The input tensor: ', input_tensor)
print('The CPU tensor: ', cpu_tensor)