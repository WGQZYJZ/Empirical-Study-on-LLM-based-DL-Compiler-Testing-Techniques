'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.half\ntorch.Tensor.half(_input_tensor, memory_format=torch.preserve_format)\n'
import torch
import torch.nn as nn
from torch.autograd import Variable
import numpy as np
batch_size = 1
input_channel = 3
input_height = 224
input_width = 224
input_tensor = np.random.rand(batch_size, input_channel, input_height, input_width)
input_tensor = torch.from_numpy(input_tensor).float()
half_tensor = input_tensor.half()
print('The input tensor is:', input_tensor)
print('The half tensor is:', half_tensor)