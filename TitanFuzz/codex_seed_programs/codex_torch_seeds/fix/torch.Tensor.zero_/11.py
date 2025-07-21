'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.zero_\ntorch.Tensor.zero_(_input_tensor)\n'
import torch
_input_tensor = torch.randn(2, 3)
print('input tensor: ', _input_tensor)
torch.Tensor.zero_(_input_tensor)
print('output tensor: ', _input_tensor)
_expected_tensor = torch.zeros(2, 3)
print('expected tensor: ', _expected_tensor)
if torch.equal(_input_tensor, _expected_tensor):
    print('Test Passed!')
else:
    print('Test Failed!')