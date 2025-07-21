'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.outer\ntorch.Tensor.outer(_input_tensor, vec2)\n'
import torch
vec1 = torch.arange(1, 11)
vec2 = torch.arange(11, 21)
result = torch.Tensor.outer(vec1, vec2)
print(result)