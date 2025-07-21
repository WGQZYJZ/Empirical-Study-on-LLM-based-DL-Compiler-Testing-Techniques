'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.take\ntorch.take(input, index)\n'
import torch
input = torch.randn(4, 6)
print('input: ', input)
index = torch.LongTensor([[0, 1], [2, 3]])
print('index: ', index)
output = torch.take(input, index)
print('output: ', output)