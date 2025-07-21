'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.view_as\ntorch.Tensor.view_as(_input_tensor, other)\n'
import torch
if True:
    import torch
    _input_tensor = torch.arange(1, 17).view(4, 4)
    print('Input tensor: \n{}'.format(_input_tensor))
    _other = torch.arange(1, 9).view(2, 4)
    _output_tensor = _input_tensor.view_as(_other)
    print('Output tensor: \n{}'.format(_output_tensor))