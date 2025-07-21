'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.qscheme\ntorch.Tensor.qscheme(_input_tensor)\n'
import torch
import numpy as np
tensor_1 = torch.randn(5, 5)
tensor_2 = torch.randn(5, 5)
tensor_3 = torch.randn(5, 5)
result_1 = tensor_1.qscheme()
result_2 = tensor_2.qscheme()
result_3 = tensor_3.qscheme()
print('tensor_1.qscheme():', result_1)
print('tensor_2.qscheme():', result_2)
print('tensor_3.qscheme():', result_3)
print('type(tensor_1.qscheme()):', type(result_1))
print('type(tensor_2.qscheme()):', type(result_2))