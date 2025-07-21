'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.square\ntorch.Tensor.square(_input_tensor)\n'
import torch
input_tensor = torch.randn(1, 3, 224, 224)
output_tensor = torch.Tensor.square(input_tensor)
print('output_tensor: ', output_tensor)