'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.element_size\ntorch.Tensor.element_size(_input_tensor)\n'
import torch
_input_tensor = torch.randn(2, 3)
print(torch.Tensor.element_size(_input_tensor))