'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.tanh\ntorch.Tensor.tanh(_input_tensor)\n'
import torch
import numpy as np
import torch
_input_data = np.array([[0, (- 1)], [1, (- 2)], [(- 1), 1], [2, 1]])
_input_tensor = torch.from_numpy(_input_data)
_output_tensor = torch.Tensor.tanh(_input_tensor)
print(_output_tensor)