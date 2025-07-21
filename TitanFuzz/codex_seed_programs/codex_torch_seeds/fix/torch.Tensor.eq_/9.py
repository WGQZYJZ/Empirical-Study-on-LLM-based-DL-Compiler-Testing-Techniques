'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.eq_\ntorch.Tensor.eq_(_input_tensor, other)\n'
import torch
input_tensor = torch.rand(3, 3)
input_tensor.eq_(0.5)
print('input_tensor = \n', input_tensor)
print('input_tensor.eq_(0.5) = \n', input_tensor.eq_(0.5))