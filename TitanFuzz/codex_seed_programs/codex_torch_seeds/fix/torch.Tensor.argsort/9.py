'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.argsort\ntorch.Tensor.argsort(_input_tensor, dim=-1, descending=False)\n'
import torch
import numpy as np
data = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print('Input data:\n{}'.format(data))
_input_tensor = torch.from_numpy(data)
print('Input tensor:\n{}'.format(_input_tensor))
_output_tensor = _input_tensor.argsort(dim=(- 1), descending=False)
print('Output tensor:\n{}'.format(_output_tensor))