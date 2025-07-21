'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.sparse_mask\ntorch.Tensor.sparse_mask(_input_tensor, mask)\n'
import torch
'\nTask 1: import PyTorch\n'
import torch
'\nTask 2: Generate input data\n'
_input_tensor = torch.tensor([[0, 1, 2, 3], [4, 5, 6, 7], [8, 9, 10, 11]])
_mask = torch.tensor([[0, 0, 0, 1], [0, 0, 1, 1], [0, 1, 1, 1]])
'\nTask 3: Call the API torch.Tensor.sparse_mask\ntorch.Tensor.sparse_mask(_input_tensor, mask)\n'
result = torch.Tensor.sparse_mask(_input_tensor, _mask)
print(result)