'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.signbit\ntorch.Tensor.signbit(_input_tensor)\n'
import torch
input_tensor = torch.randn(4, 4)
print('Input Tensor: ', input_tensor)
signbit_result = input_tensor.signbit()
print('Signbit Result: ', signbit_result)