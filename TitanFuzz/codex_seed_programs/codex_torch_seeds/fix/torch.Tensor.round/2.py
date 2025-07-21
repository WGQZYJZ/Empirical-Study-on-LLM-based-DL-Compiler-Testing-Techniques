'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.round\ntorch.Tensor.round(_input_tensor)\n'
import torch
if True:
    _input_tensor = torch.randn(4, 4)
    _output_tensor = torch.Tensor.round(_input_tensor)
    print('input_tensor:', _input_tensor)
    print('output_tensor:', _output_tensor)