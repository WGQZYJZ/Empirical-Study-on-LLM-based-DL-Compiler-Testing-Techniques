'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.is_cuda\ntorch.Tensor.is_cuda(_input_tensor, )\n'
import torch
_input_tensor = torch.randn(2, 3)
print(_input_tensor)
print(torch.Tensor.is_cuda(_input_tensor))
_input_tensor = torch.randn(2, 3).cuda()
print(_input_tensor)
print(torch.Tensor.is_cuda(_input_tensor))