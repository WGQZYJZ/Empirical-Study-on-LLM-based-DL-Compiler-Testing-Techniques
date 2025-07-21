'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.device\ntorch.Tensor.device(_input_tensor, )\n'
import torch
data = torch.randn(1, 1, 3, 3, 3)
print(torch.Tensor.device(data))