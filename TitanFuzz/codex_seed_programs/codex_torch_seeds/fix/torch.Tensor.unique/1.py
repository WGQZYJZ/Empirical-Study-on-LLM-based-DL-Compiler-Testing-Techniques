'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.unique\ntorch.Tensor.unique(_input_tensor, sorted=True, return_inverse=False, return_counts=False, dim=None)\n'
import torch
_input_tensor = torch.tensor([[1, 3, 3, 3, 1, 2, 2, 3, 1, 2], [4, 4, 4, 4, 4, 4, 4, 4, 4, 4]])
_output_tensor = torch.Tensor.unique(_input_tensor, sorted=True, return_inverse=False, return_counts=False, dim=None)
print(_output_tensor)