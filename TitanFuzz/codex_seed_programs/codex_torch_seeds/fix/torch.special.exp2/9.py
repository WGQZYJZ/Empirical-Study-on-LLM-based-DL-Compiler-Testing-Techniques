'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.special.exp2\ntorch.special.exp2(input, *, out=None)\n'
import torch
x = torch.tensor([(- 3.0), (- 2.0), (- 1.0), 0.0, 1.0, 2.0, 3.0])
y = torch.special.exp2(x)
print('The input tensor: ', x)
print('The output tensor: ', y)