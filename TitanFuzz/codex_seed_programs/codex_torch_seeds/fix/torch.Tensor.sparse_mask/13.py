'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.sparse_mask\ntorch.Tensor.sparse_mask(_input_tensor, mask)\n'
import torch
import torch
_input_tensor = torch.tensor([[1, 2, 3], [4, 5, 6]])
mask = torch.tensor([[True, True, False], [False, True, True]])
_output = torch.Tensor.sparse_mask(_input_tensor, mask)
print(_output)