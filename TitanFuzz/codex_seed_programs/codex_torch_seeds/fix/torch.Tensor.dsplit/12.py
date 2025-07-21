'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.dsplit\ntorch.Tensor.dsplit(_input_tensor, split_size_or_sections)\n'
import torch
x = torch.randn(4, 6)
print(x)
result = torch.Tensor.dsplit(x, 2)
print(result)
result = torch.Tensor.dsplit(x, [2, 3])
print(result)