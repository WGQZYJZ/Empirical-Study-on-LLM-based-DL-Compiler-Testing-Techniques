'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.clip\ntorch.Tensor.clip(_input_tensor, min=None, max=None)\n'
import torch
x = torch.Tensor([[(- 0.1), (- 0.2), 0.3, 0.4], [0.5, 0.6, 0.7, 0.8]])
print('Input data:')
print(x)
y = x.clip(min=0, max=1)
print('Output data:')
print(y)