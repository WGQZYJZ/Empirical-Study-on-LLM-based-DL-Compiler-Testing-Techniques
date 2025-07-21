'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.renorm\ntorch.Tensor.renorm(_input_tensor, p, dim, maxnorm)\n'
import torch
data = torch.randn(2, 3)
print(data)
print(data.renorm(1, 0, 3))
print(data.renorm(2, 0, 3))
print(data.renorm(1, 1, 3))
print(data.renorm(2, 1, 3))
'\nTask 4: Call the API torch.Tensor.renorm_\ntorch.Tensor.renorm_(input_tensor, p, dim, maxnorm)\n'
print(data)
print(data.renorm_(1, 0, 3))
print(data.renorm_(2, 0, 3))
print(data.renorm_(1, 1, 3))
print(data.renorm_(2, 1, 3))