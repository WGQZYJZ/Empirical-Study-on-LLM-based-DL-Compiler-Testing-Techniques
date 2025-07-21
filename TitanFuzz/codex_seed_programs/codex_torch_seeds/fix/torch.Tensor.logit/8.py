'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.logit\ntorch.Tensor.logit(_input_tensor)\n'
import torch
input_tensor = torch.randn(2, 3)
print(f'Input tensor: {input_tensor}')
output_tensor = torch.Tensor.logit(input_tensor)
print(f'Output tensor: {output_tensor}')