'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.outer\ntorch.Tensor.outer(_input_tensor, vec2)\n'
import torch
vec1 = torch.tensor([1, 2, 3])
vec2 = torch.tensor([0, 1, 0])
torch.Tensor.outer(vec1, vec2)