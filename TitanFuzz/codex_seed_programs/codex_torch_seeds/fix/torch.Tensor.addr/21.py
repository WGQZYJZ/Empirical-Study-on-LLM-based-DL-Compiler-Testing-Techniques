'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.addr\ntorch.Tensor.addr(_input_tensor, vec1, vec2, *, beta=1, alpha=1)\n'
import torch
input_data = torch.randn(3, 4)
vec1 = torch.randn(4)
vec2 = torch.randn(3)
output = torch.Tensor.addr(input_data, vec1, vec2)
print(output)