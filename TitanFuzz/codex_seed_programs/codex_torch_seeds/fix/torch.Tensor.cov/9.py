'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.cov\ntorch.Tensor.cov(_input_tensor, *, correction=1, fweights=None, aweights=None)\n'
import torch
input_tensor = torch.rand(10, 3)
print(input_tensor)
cov_result = torch.Tensor.cov(input_tensor)
print(cov_result)
cov_result_2 = torch.Tensor.cov(input_tensor, correction=0)
print(cov_result_2)