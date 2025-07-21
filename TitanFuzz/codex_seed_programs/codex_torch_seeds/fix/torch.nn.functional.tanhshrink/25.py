'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.functional.tanhshrink\ntorch.nn.functional.tanhshrink(input)\n'
import torch
input = torch.randn(4, 4)
print('Input: ', input)
output = torch.nn.functional.tanhshrink(input)
print('Output: ', output)