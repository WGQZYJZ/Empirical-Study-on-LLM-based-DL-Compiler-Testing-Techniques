'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.corrcoef\ntorch.Tensor.corrcoef(_input_tensor)\n'
import torch
from torch import Tensor
from torch.autograd import Variable
from torch.nn import functional as F
import numpy as np
input_tensor = Tensor(np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))
print(torch.Tensor.corrcoef(input_tensor))