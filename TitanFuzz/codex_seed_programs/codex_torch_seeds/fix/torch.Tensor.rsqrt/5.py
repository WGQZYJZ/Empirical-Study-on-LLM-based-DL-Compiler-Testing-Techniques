'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.rsqrt\ntorch.Tensor.rsqrt(_input_tensor)\n'
import torch
data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
input_tensor = torch.tensor(data)
print('Input tensor: ', input_tensor)
output_tensor = input_tensor.rsqrt()
print('Output tensor: ', output_tensor)