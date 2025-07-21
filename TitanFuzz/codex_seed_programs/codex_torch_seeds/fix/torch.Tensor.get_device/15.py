'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.get_device\ntorch.Tensor.get_device(_input_tensor)\n'
import torch
_input_tensor = torch.randn(2, 3, requires_grad=True)
print(torch.Tensor.get_device(_input_tensor))