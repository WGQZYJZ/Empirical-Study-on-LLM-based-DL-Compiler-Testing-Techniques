'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.digamma\ntorch.Tensor.digamma(_input_tensor)\n'
import torch
import numpy as np
import torch
input_tensor = torch.randn(2, 3, 4)
result = input_tensor.digamma()
print('The result is: ', result)