'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.is_cuda\ntorch.Tensor.is_cuda(_input_tensor, )\n'
import torch
import numpy as np
_input_tensor = torch.Tensor(np.random.rand(2, 3))
print(torch.Tensor.is_cuda(_input_tensor))
print('====End of the example====')