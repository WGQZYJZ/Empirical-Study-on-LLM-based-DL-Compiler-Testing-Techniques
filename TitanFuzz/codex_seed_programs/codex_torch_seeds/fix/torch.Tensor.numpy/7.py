'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.numpy\ntorch.Tensor.numpy(_input_tensor)\n'
import torch
input_tensor = torch.randn(1, 3, 224, 224)
print(input_tensor)
print(type(input_tensor))
output_numpy = input_tensor.numpy()
print(output_numpy)
print(type(output_numpy))