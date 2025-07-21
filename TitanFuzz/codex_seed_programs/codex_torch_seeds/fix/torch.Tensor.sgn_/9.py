'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.sgn_\ntorch.Tensor.sgn_(_input_tensor)\n'
import torch
input_tensor = torch.randn(3, 3)
print('Input tensor: ', input_tensor)
torch.Tensor.sgn_(input_tensor)
print('Output tensor: ', input_tensor)
if torch.equal(input_tensor, torch.sign(input_tensor)):
    print('Output is correct')
else:
    print('Output is incorrect')