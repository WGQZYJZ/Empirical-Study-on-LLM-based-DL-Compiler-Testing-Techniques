'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.cholesky\ntorch.Tensor.cholesky(_input_tensor, upper=False)\n'
import torch
_input_tensor = torch.rand(3, 3)
cholesky_tensor = _input_tensor.cholesky()
print('The cholesky decomposition of the input tensor is: ', cholesky_tensor)