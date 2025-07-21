'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.clamp_\ntorch.Tensor.clamp_(_input_tensor, min=None, max=None)\n'
import torch
if True:
    _input_tensor = torch.tensor([(- 1), 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
    print('Input tensor: {}'.format(_input_tensor))
    _output_tensor = _input_tensor.clamp_(min=0, max=5)
    print('Output tensor: {}'.format(_output_tensor))