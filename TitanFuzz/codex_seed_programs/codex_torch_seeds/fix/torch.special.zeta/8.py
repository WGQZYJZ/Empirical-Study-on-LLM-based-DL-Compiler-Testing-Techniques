'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.special.zeta\ntorch.special.zeta(input, other, *, out=None)\n'
import torch
input_data = torch.randn(4, 4)
other_data = torch.randn(4, 4)
output = torch.special.zeta(input_data, other_data)
print('The output is: ', output)