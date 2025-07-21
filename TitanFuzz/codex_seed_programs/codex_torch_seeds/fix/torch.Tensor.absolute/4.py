'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.absolute\ntorch.Tensor.absolute(_input_tensor)\n'
import torch
_input_tensor = torch.randint(10, (2, 3), dtype=torch.float32)
print('Input tensor: {}'.format(_input_tensor))
_output_tensor = torch.Tensor.absolute(_input_tensor)
print('Output tensor: {}'.format(_output_tensor))