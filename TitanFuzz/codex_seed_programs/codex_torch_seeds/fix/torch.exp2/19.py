'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.exp2\ntorch.exp2(input, *, out=None)\n'
import torch
import torch
input_data = torch.tensor([1.0, 2.0, 3.0])
output = torch.exp2(input_data)
print('The result of exp2 is: {}'.format(output))