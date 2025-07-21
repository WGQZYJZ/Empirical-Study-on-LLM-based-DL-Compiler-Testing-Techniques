'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.t_\ntorch.Tensor.t_(_input_tensor)\n'
import torch
from torch.autograd import Variable
import numpy as np
input_tensor = np.array([[1, 2, 3], [4, 5, 6]])
input_tensor = torch.from_numpy(input_tensor)
torch.Tensor.t_(input_tensor)
print(input_tensor)