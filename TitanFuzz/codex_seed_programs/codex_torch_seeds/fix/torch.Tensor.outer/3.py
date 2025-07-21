'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.outer\ntorch.Tensor.outer(_input_tensor, vec2)\n'
import torch
input_tensor = torch.tensor([[1, 2, 3], [4, 5, 6]])
vec2 = torch.tensor([1, 2, 3])
output_tensor = input_tensor.outer(vec2)
print('input tensor:', input_tensor)
print('vec2:', vec2)
print('output tensor:', output_tensor)