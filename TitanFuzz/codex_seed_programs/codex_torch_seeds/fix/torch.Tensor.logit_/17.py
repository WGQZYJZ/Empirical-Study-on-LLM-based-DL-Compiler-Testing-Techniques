'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.logit_\ntorch.Tensor.logit_(_input_tensor)\n'
import torch
input_tensor = torch.randn(2, 3)
logit_output = torch.Tensor.logit_(input_tensor)
print('The input tensor is: \n{}'.format(input_tensor))
print('The output tensor is: \n{}'.format(logit_output))