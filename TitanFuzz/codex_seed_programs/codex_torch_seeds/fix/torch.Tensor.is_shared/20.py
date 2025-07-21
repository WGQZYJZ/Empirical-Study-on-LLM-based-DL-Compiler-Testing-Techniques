'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.is_shared\ntorch.Tensor.is_shared(_input_tensor, )\n'
import torch
input_tensor = torch.randn(1, 2, 3)
print(torch.Tensor.is_shared(input_tensor))
input_tensor.share_memory_()
print(torch.Tensor.is_shared(input_tensor))