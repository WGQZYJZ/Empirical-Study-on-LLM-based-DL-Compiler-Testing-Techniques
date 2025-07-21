'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.ravel\ntorch.Tensor.ravel(_input_tensor)\n'
import torch
input_tensor = torch.randint(0, 10, (3, 2, 3))
output_tensor = input_tensor.ravel()
print(input_tensor)
print(output_tensor)