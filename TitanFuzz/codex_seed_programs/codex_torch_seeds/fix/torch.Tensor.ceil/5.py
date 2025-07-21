'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.ceil\ntorch.Tensor.ceil(_input_tensor)\n'
import torch
input_data = [1.1, 2.5, 3.5, 4.5, 5.5, 6.5, 7.5, 8.5, 9.5]
input_tensor = torch.tensor(input_data)
output_tensor = input_tensor.ceil()
print('Input tensor: {}'.format(input_tensor))
print('Output tensor: {}'.format(output_tensor))