'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.unique_consecutive\ntorch.Tensor.unique_consecutive(_input_tensor, return_inverse=False, return_counts=False, dim=None)\n'
import torch
_input_tensor = torch.randint(low=0, high=9, size=(4, 4), dtype=torch.int32)
print(_input_tensor)
print(torch.Tensor.unique_consecutive(_input_tensor, return_inverse=True, return_counts=True, dim=0))