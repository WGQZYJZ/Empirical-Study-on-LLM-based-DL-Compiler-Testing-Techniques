'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.cpu\ntorch.Tensor.cpu(_input_tensor, memory_format=torch.preserve_format)\n'
import torch
input_tensor = torch.rand(100, 100)
cpu_output = torch.Tensor.cpu(input_tensor)
print(cpu_output)