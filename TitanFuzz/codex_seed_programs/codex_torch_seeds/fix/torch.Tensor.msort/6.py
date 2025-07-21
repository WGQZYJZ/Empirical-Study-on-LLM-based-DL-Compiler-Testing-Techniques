'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.msort\ntorch.Tensor.msort(_input_tensor)\n'
import torch
_input_tensor = torch.randn(3, 3)
print('input tensor is: \n', _input_tensor)
_sorted_tensor = torch.Tensor.msort(_input_tensor)
print('sorted tensor is: \n', _sorted_tensor)