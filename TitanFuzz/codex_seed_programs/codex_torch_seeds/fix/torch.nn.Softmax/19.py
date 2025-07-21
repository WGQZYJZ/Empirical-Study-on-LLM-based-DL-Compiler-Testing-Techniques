'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.Softmax\ntorch.nn.Softmax(dim=None)\n'
import torch
input_data = torch.randn(2, 3)
print('Input data: \n', input_data)
softmax = torch.nn.Softmax(dim=1)
output = softmax(input_data)
print('Output: \n', output)
print('Sum of output: \n', output.sum(dim=1))