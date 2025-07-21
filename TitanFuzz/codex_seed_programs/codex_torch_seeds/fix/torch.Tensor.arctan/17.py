'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.arctan\ntorch.Tensor.arctan(_input_tensor)\n'
import torch
import numpy as np
_input_tensor = torch.Tensor([(np.pi / 2), (np.pi / 3), (np.pi / 4), (np.pi / 6)])
_output_tensor = torch.Tensor.arctan(_input_tensor)
print('The output tensor is:', _output_tensor)