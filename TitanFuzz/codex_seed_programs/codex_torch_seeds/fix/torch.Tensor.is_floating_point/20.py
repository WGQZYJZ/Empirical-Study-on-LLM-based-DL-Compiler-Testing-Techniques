'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.is_floating_point\ntorch.Tensor.is_floating_point(_input_tensor)\n'
import torch
import torch
input_tensor = torch.randn(5, 3)
print(input_tensor)
print(torch.Tensor.is_floating_point(input_tensor))
print(torch.Tensor.is_floating_point(torch.tensor([1, 2, 3])))
print(torch.Tensor.is_floating_point(torch.tensor([1.1, 2.2, 3.3])))
print(torch.Tensor.is_floating_point(torch.tensor([1, 2, 3], dtype=torch.float32)))