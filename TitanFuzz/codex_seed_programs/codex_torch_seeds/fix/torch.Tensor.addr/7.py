'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.addr\ntorch.Tensor.addr(_input_tensor, vec1, vec2, *, beta=1, alpha=1)\n'
import torch
input_tensor = torch.randn(3, 5)
vec1 = torch.randn(5)
vec2 = torch.randn(3)
result = torch.Tensor.addr(input_tensor, vec1, vec2, beta=1, alpha=1)
print('The result is: ', result)