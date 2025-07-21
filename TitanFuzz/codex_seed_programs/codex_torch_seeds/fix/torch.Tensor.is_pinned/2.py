'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.is_pinned\ntorch.Tensor.is_pinned(_input_tensor, )\n'
import torch
if True:
    _input_tensor = torch.rand(10)
    _output_tensor = torch.Tensor.is_pinned(_input_tensor)
    print('PyTorch Version:', torch.__version__)
    print('Output Tensor:', _output_tensor)