'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.masked_fill\ntorch.Tensor.masked_fill(_input_tensor, mask, value)\n'
import torch
_input_tensor = torch.rand(4, 4)
_mask = torch.ByteTensor([[0, 0, 1, 0], [1, 0, 1, 0], [1, 0, 1, 0], [0, 0, 0, 0]])
_value = (- 1)
_input_tensor.masked_fill(_mask, _value)
print(_input_tensor)