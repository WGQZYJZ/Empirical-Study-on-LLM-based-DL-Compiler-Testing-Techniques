'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.is_floating_point\ntorch.is_floating_point(input)\n'
import torch
input1 = torch.tensor([1, 2, 3, 4, 5])
input2 = torch.tensor([1.1, 2.2, 3.3, 4.4, 5.5])
print('input1 is floating point:', torch.is_floating_point(input1))
print('input2 is floating point:', torch.is_floating_point(input2))
'\nExpected output:\ninput1 is floating point: False\ninput2 is floating point: True\n'