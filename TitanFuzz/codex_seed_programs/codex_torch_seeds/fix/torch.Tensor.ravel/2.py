'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.ravel\ntorch.Tensor.ravel(_input_tensor)\n'
import torch
input_data = torch.arange(0, 12)
input_data = input_data.view(3, 4)
output_data = input_data.ravel()
print('The input data is: ', input_data)
print('The output data is: ', output_data)