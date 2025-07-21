'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.dist\ntorch.Tensor.dist(_input_tensor, other, p=2)\n'
import torch
tensor_a = torch.tensor([1, 2, 3])
tensor_b = torch.tensor([4, 5, 6])
result = tensor_a.dist(tensor_b)
print(result)
result = tensor_a.dist(tensor_b, p=3)
print(result)