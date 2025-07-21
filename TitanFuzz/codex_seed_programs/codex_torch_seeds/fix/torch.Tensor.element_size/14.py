'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.element_size\ntorch.Tensor.element_size(_input_tensor)\n'
import torch
import sys
import numpy as np
input_tensor = torch.randn(3, 4)
element_size = input_tensor.element_size()
print('input_tensor:', input_tensor)
print('element_size:', element_size)