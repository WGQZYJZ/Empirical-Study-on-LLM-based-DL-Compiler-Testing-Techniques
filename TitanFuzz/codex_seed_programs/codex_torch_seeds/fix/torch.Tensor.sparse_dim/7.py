'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.sparse_dim\ntorch.Tensor.sparse_dim(_input_tensor)\n'
import torch
from torch.autograd import Variable
if True:
    import torch
    _input_tensor = torch.randn((2, 3))
    print('Input tensor:')
    print(_input_tensor)
    _sparse_dim = torch.Tensor.sparse_dim(_input_tensor)
    print('Output sparse_dim:')
    print(_sparse_dim)