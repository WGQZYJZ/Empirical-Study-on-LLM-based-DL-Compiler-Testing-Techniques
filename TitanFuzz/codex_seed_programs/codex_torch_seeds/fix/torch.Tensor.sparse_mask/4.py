'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.sparse_mask\ntorch.Tensor.sparse_mask(_input_tensor, mask)\n'
import torch
from torch.autograd import Variable
import numpy as np
import torch
from torch.autograd import Variable
import numpy as np
input_tensor = torch.randn(3, 3, 3)
print(input_tensor)
mask = torch.tensor([[0, 0, 1], [1, 0, 0], [0, 1, 1]])
output_tensor = torch.Tensor.sparse_mask(input_tensor, mask)
print(output_tensor)