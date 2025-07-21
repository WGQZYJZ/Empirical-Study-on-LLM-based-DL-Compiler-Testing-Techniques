'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.masked_fill_\ntorch.Tensor.masked_fill_(_input_tensor, mask, value\n'
import torch
from torch import nn
from torch.nn import functional as F
import torch
from torch import nn
from torch.nn import functional as F
input_tensor = torch.randint(low=0, high=10, size=(2, 3, 4))
print('Input tensor:\n', input_tensor)
mask = torch.tensor([[0, 0, 1, 0], [0, 0, 0, 0], [0, 1, 0, 0]], dtype=torch.bool)
print('Mask:\n', mask)
filled_tensor = input_tensor.masked_fill_(mask, (- 1))
print('Filled tensor:\n', filled_tensor)