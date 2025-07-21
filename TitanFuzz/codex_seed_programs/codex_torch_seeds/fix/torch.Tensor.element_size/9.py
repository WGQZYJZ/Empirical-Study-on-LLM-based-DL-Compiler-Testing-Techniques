'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.element_size\ntorch.Tensor.element_size(_input_tensor)\n'
import torch
_input_tensor = torch.randn(2, 3, 5)
print(torch.Tensor.element_size(_input_tensor))
print(torch.Tensor.element_size(torch.randn(2, 3, 5)))
print(torch.Tensor.element_size(torch.randn(2, 3, 5, 6)))
print(torch.Tensor.element_size(torch.randn(2, 3, 5, 6, 7)))
print(torch.Tensor.element_size(torch.randn(2, 3, 5, 6, 7, 8)))
print(torch.Tensor.element_size(torch.randn(2, 3, 5, 6, 7, 8, 9)))