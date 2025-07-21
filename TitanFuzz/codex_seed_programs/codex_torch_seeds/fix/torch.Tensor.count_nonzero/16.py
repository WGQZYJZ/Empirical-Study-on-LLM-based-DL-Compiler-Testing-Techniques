'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.count_nonzero\ntorch.Tensor.count_nonzero(_input_tensor, dim=None)\n'
import torch
import numpy as np
if True:
    input_tensor = torch.Tensor(np.random.randint(0, 2, size=(2, 3, 3)))
    print('input_tensor: \n', input_tensor)
    output_tensor = input_tensor.count_nonzero()
    print('output_tensor: \n', output_tensor)