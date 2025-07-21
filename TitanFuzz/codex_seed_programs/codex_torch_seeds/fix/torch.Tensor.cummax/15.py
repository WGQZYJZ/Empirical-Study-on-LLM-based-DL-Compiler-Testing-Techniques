'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.cummax\ntorch.Tensor.cummax(_input_tensor, dim)\n'
import torch
import torch
_input_tensor = torch.tensor([[1, 2, 3], [1, 3, 2], [3, 2, 1]])
_output_tensor = torch.Tensor.cummax(_input_tensor, dim=1)
print(_output_tensor)