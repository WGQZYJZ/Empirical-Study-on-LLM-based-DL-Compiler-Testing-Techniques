'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.logdet\ntorch.Tensor.logdet(_input_tensor)\n'
import torch
input_tensor = torch.rand(2, 2)
output_tensor = torch.Tensor.logdet(input_tensor)
print(output_tensor)