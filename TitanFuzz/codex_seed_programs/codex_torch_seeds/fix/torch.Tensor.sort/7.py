'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.sort\ntorch.Tensor.sort(_input_tensor, dim=-1, descending=False)\n'
import torch
tensor = torch.randn(2, 3)
print(tensor)
tensor2 = torch.Tensor.sort(tensor, dim=(- 1), descending=False)
print(tensor2)
tensor3 = torch.Tensor.sort(tensor, dim=(- 1), descending=True)
print(tensor3)