'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.view\ntorch.Tensor.view(_input_tensor, *shape)\n'
import torch
_input_tensor = torch.randn(2, 3, 4)
_view_tensor = _input_tensor.view(2, 12)
print(_view_tensor)
_view_tensor = _input_tensor.view(2, (- 1))
print(_view_tensor)
_view_tensor = _input_tensor.view((- 1), 12)
print(_view_tensor)