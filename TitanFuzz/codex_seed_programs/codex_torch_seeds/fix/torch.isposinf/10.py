'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.isposinf\ntorch.isposinf(input, *, out=None)\n'
import torch
input_data = torch.Tensor([float('inf'), float('-inf'), float('nan'), (- 1), 0, 1])
result = torch.isposinf(input_data)
print('Input: ', input_data)
print('Output: ', result)