'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.is_signed\ntorch.Tensor.is_signed(_input_tensor)\n'
import torch
import numpy as np
_input_tensor = torch.tensor([[(- 1.0), 2.0, (- 3.0), 4.0], [5.0, (- 6.0), 7.0, (- 8.0)]])
_result = torch.Tensor.is_signed(_input_tensor)
print('The result of is_signed: ', _result)