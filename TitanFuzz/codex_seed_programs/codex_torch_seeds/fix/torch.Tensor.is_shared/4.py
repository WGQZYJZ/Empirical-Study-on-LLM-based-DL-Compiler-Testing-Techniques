'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.is_shared\ntorch.Tensor.is_shared(_input_tensor, )\n'
import torch
input_tensor = torch.randn(3, 3)
print(input_tensor.is_shared())
input_tensor_shared = torch.randn(3, 3).share_memory_()
print(input_tensor_shared.is_shared())