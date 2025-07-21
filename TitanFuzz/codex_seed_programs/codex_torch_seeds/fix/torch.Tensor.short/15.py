'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.short\ntorch.Tensor.short(_input_tensor, memory_format=torch.preserve_format)\n'
import torch
import numpy as np
input_tensor = torch.tensor(np.random.rand(2, 3, 4, 5), dtype=torch.float32)
print('Input Tensor: ', input_tensor)
output_tensor = input_tensor.short()
print('Output Tensor: ', output_tensor)
'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.size\ntorch.Tensor.size(_input_tensor, dim=None)\n'
import torch
import numpy as np
input_tensor = torch.tensor(np.random.rand(2, 3, 4, 5), dtype=torch.float32)
print('Input Tensor: ', input_tensor)
output_tensor = input_tensor.size()
print('Output Tensor: ', output_tensor)