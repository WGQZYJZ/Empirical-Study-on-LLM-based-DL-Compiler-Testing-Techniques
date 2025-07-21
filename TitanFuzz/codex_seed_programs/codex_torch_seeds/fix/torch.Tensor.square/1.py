'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.square\ntorch.Tensor.square(_input_tensor)\n'
import torch
input_tensor = torch.rand(2, 3)
result = input_tensor.square()
print('The result is: ', result)