'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.tolist\ntorch.Tensor.tolist(_input_tensor)\n'
import torch
input_tensor = torch.randn(2, 3)
output_list = input_tensor.tolist()
print('The result is: ', output_list)