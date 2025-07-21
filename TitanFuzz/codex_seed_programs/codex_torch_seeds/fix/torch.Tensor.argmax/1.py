'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.argmax\ntorch.Tensor.argmax(_input_tensor, dim=None, keepdim=False)\n'
import torch
input_tensor = torch.randn(3, 2)
print('input_tensor: {}'.format(input_tensor))
print('index of max value in each row: {}'.format(torch.Tensor.argmax(input_tensor, dim=1)))
print('index of max value in each column: {}'.format(torch.Tensor.argmax(input_tensor, dim=0)))
print('index of max value in each row with keeping the dimension: {}'.format(torch.Tensor.argmax(input_tensor, dim=1, keepdim=True)))
print('index of max value in each column with keeping the dimension: {}'.format(torch.Tensor.argmax(input_tensor, dim=0, keepdim=True)))