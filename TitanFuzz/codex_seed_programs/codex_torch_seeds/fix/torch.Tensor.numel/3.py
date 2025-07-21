'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.numel\ntorch.Tensor.numel(_input_tensor)\n'
import torch
tensor = torch.randn(4, 4)
print(tensor.numel())