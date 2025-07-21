import torch
from torch import nn
from torch.autograd import Variable
if True:
    import torch
    _input_tensor = torch.randn(3, 3)
    print('Input tensor: ')
    print(_input_tensor)
    _output_tensor = torch.Tensor.to_sparse(_input_tensor, sparseDims=2)
    print('Output tensor: ')
    print(_output_tensor)