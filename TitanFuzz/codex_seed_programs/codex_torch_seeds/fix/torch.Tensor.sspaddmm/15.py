'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.sspaddmm\ntorch.Tensor.sspaddmm(_input_tensor, mat1, mat2, *, beta=1, alpha=1)\n'
import torch
import numpy as np
if True:
    print('Test sspaddmm')
    input_tensor = torch.rand(1024, 1024)
    mat1 = torch.rand(1024, 1024)
    mat2 = torch.rand(1024, 1024)
    print(torch.Tensor.sspaddmm(input_tensor, mat1, mat2))