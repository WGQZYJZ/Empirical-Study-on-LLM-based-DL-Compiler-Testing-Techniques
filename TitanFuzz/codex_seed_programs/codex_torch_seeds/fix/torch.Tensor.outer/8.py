'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.outer\ntorch.Tensor.outer(_input_tensor, vec2)\n'
import torch
vec1 = torch.tensor([1, 2, 3, 4])
vec2 = torch.tensor([5, 6, 7, 8])
out = torch.Tensor.outer(vec1, vec2)
print('The output tensor: \n', out)