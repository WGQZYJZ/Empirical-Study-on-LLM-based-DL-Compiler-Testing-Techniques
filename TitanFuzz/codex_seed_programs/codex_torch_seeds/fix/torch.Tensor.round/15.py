'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.round\ntorch.Tensor.round(_input_tensor)\n'
import torch
input_tensor = torch.tensor([[1.2, 2.3, 3.4], [4.5, 5.6, 6.7]])
output_tensor = torch.Tensor.round(input_tensor)
print('output_tensor: ', output_tensor)