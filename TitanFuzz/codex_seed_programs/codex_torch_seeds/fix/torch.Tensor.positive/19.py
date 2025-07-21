'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.positive\ntorch.Tensor.positive(_input_tensor)\n'
import torch
input_tensor = torch.randn(3, 3)
print('Input tensor:')
print(input_tensor)
print('Positive tensor:')
print(input_tensor.positive())