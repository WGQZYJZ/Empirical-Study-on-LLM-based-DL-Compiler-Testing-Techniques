'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.byte\ntorch.Tensor.byte(_input_tensor, memory_format=torch.preserve_format)\n'
import torch
import numpy as np
_input_tensor = torch.rand(2, 3)
_output_tensor = _input_tensor.byte()
print('The input tensor is:', _input_tensor)
print('The output tensor is:', _output_tensor)