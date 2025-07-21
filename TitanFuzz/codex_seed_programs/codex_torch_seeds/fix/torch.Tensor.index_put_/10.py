'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.index_put_\ntorch.Tensor.index_put_(_input_tensor, indices, values, accumulate=False)\n'
import torch
import numpy as np
if True:
    input_tensor = torch.tensor([[1, 2, 3], [4, 5, 6]])
    print('Original tensor: \n{}'.format(input_tensor))
    indices = torch.tensor([1, 2, 3, 4, 5, 6])
    values = torch.tensor([10, 20, 30, 40, 50, 60])
    input_tensor.index_put_((indices - 1), values)
    print('Updated tensor: \n{}'.format(input_tensor))