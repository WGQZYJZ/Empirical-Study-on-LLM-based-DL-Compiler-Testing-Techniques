'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.real\ntorch.Tensor.real(_input_tensor, )\n'
import torch
if True:
    input_tensor = torch.randn(2, 3, 4)
    print(f'Input Tensor: {input_tensor}')
    print(f'Real part of input tensor: {torch.Tensor.real(input_tensor)}')