'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.dsplit\ntorch.dsplit(input, indices_or_sections)\n'
import torch
a = torch.randn(5, 5, 5)
result = torch.dsplit(a, 5)
print('result: ', result)
print('result size: ', result[0].size())