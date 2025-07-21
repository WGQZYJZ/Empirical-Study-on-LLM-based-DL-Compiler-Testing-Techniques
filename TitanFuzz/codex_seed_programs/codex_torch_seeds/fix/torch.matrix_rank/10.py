'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.matrix_rank\ntorch.matrix_rank(input, tol=None, symmetric=False, *, out=None)\n'
import torch
if True:
    input = torch.randn(3, 3)
    print('Input data: ', input)
    output = torch.matrix_rank(input)
    print('Output: ', output)