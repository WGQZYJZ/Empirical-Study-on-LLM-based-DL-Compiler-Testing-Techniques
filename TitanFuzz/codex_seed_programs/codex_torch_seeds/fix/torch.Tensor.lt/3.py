'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.lt\ntorch.Tensor.lt(_input_tensor, other)\n'
import torch
input_tensor = torch.randint(low=0, high=10, size=(3, 3))
print('Input tensor: ')
print(input_tensor)
output_tensor = input_tensor.lt(5)
print('Output tensor: ')
print(output_tensor)