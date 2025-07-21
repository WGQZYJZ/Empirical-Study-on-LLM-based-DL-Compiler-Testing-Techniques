'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.is_cuda\ntorch.Tensor.is_cuda(_input_tensor, )\n'
import torch
_input_tensor = torch.rand(1, 1, 1, 1)
print(torch.Tensor.is_cuda(_input_tensor))