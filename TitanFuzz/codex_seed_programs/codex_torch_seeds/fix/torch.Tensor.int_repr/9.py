'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.int_repr\ntorch.Tensor.int_repr(_input_tensor)\n'
import torch
_input_tensor = torch.randint(low=0, high=10, size=(2, 3), dtype=torch.int64)
print('Input tensor: {}'.format(_input_tensor))
_output_tensor = _input_tensor.int_repr()
print('Output tensor: {}'.format(_output_tensor))