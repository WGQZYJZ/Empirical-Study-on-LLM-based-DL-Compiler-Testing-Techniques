'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.neg\ntorch.neg(input, *, out=None)\n'
import torch
input_data = torch.randn(5, 3)
print('Input data:')
print(input_data)
print('Negative of input data:')
print(torch.neg(input_data))
'\nTask 4: Call the API torch.abs\ntorch.abs(input, *, out=None)\n'
print('Absolute value of input data:')
print(torch.abs(input_data))
'\nTask 5: Call the API torch.sign\ntorch.sign(input, *, out=None)\n'
print('Sign of input data:')
print(torch.sign(input_data))
'\nTask 6: Call the API torch.reciprocal\ntorch.reciprocal(input, *, out=None)\n'
print('Reciprocal of input data:')
print(torch.reciprocal(input_data))
'\nTask 7: Call the API torch.logical_not\ntorch.logical_not(input, *, out=None)\n'