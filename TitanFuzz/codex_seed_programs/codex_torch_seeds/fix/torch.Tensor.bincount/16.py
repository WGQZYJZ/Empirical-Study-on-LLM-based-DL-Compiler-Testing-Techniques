'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.bincount\ntorch.Tensor.bincount(_input_tensor, weights=None, minlength=0)\n'
import torch
_input_tensor = torch.tensor([0, 1, 1, 2, 2, 2, 3, 3, 3, 3])
_result_tensor = torch.Tensor.bincount(_input_tensor)
print('_result_tensor: ', _result_tensor)