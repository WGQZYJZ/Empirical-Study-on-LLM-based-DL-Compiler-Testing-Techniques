'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.logit_\ntorch.Tensor.logit_(_input_tensor)\n'
import torch
_input_tensor = torch.randn(2, 3, requires_grad=True)
_logit_output = torch.Tensor.logit_(_input_tensor)
print('Input Tensor: ', _input_tensor)
print('Output Tensor: ', _logit_output)