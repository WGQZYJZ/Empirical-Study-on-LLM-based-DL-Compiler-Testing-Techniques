'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.matmul\ntorch.Tensor.matmul(_input_tensor, tensor2)\n'
import torch
_input_tensor = torch.rand(10, 3)
print(_input_tensor)
tensor2 = torch.rand(3, 4)
print(torch.Tensor.matmul(_input_tensor, tensor2))