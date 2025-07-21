'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.ConstantPad1d\ntorch.nn.ConstantPad1d(padding, value)\n'
import torch
input = torch.tensor([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]], dtype=torch.float)
print('input: ', input)
padding = (1, 2)
value = 0
result = torch.nn.ConstantPad1d(padding, value)(input)
print('result: ', result)