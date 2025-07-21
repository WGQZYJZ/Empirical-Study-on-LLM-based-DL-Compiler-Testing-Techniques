'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.is_shared\ntorch.Tensor.is_shared(_input_tensor, )\n'
import torch
_input_tensor = torch.randn(1, 2, 3, 4)
print(torch.Tensor.is_shared(_input_tensor))
_input_tensor = torch.randn(1, 2, 3, 4).share_memory_()
print(torch.Tensor.is_shared(_input_tensor))