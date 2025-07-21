'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.unfold\ntorch.Tensor.unfold(_input_tensor, dimension, size, step)\n'
import torch
import numpy as np
input_tensor = torch.arange(1, 17, dtype=torch.float32).reshape(4, 4)
print('Input tensor: \n{}'.format(input_tensor))
print('Output tensor: \n{}'.format(input_tensor.unfold(0, 2, 2)))