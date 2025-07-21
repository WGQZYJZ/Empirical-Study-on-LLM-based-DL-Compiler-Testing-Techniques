'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.device\ntorch.Tensor.device(_input_tensor, )\n'
import torch
import torch
input_tensor = torch.randn(2, 3, 4)
output_tensor = input_tensor.device('cuda')
print(output_tensor)