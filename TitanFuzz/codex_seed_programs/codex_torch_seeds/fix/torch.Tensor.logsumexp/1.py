'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.logsumexp\ntorch.Tensor.logsumexp(_input_tensor, dim, keepdim=False)\n'
import torch
input_tensor = torch.randn(2, 3)
print(input_tensor)
result_tensor = input_tensor.logsumexp(dim=0, keepdim=False)
print(result_tensor)
result_tensor = input_tensor.logsumexp(dim=1, keepdim=False)
print(result_tensor)
result_tensor = input_tensor.logsumexp(dim=0, keepdim=True)
print(result_tensor)
result_tensor = input_tensor.logsumexp(dim=1, keepdim=True)
print(result_tensor)