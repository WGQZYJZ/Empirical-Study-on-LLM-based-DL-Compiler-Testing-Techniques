import torch
from torch import nn
from torch.autograd import Variable
_input_tensor = torch.randn(2, 3)
torch.Tensor.zero_(_input_tensor)
_expected_tensor = torch.zeros(2, 3)
if torch.equal(_input_tensor, _expected_tensor):
    print('Test Passed!')
else:
    print('Test Failed!')