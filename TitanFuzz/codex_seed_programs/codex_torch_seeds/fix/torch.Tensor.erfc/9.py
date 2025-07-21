'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.erfc\ntorch.Tensor.erfc(_input_tensor)\n'
import torch
input_tensor = torch.tensor([0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0])
output_tensor = input_tensor.erfc()
print('input tensor: ', input_tensor)
print('output tensor: ', output_tensor)