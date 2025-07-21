'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.count_nonzero\ntorch.Tensor.count_nonzero(_input_tensor, dim=None)\n'
import torch
import torch
_input_tensor = torch.randint(low=0, high=2, size=(5, 5), dtype=torch.int)
_count_nonzero_tensor = torch.Tensor.count_nonzero(_input_tensor, dim=None)
print('count_nonzero_tensor:', _count_nonzero_tensor)