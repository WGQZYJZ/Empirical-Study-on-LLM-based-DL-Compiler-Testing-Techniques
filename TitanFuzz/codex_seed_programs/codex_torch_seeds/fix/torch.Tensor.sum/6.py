'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.sum\ntorch.Tensor.sum(_input_tensor, dim=None, keepdim=False, dtype=None)\n'
import torch
if True:
    _input_tensor = torch.ones(3, 3)
    print('Input tensor: {}'.format(_input_tensor))
    _sum_all_elements = _input_tensor.sum()
    print('Sum of all elements: {}'.format(_sum_all_elements))
    _sum_all_elements_dim0 = _input_tensor.sum(dim=0)
    print('Sum of all elements along dimension 0: {}'.format(_sum_all_elements_dim0))
    _sum_all_elements_dim1 = _input_tensor.sum(dim=1)