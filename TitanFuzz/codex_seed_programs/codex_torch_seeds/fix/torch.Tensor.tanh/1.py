'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.tanh\ntorch.Tensor.tanh(_input_tensor)\n'
import torch
input_tensor = torch.randn(5)
output_tensor = input_tensor.tanh()
print(input_tensor)
print(output_tensor)