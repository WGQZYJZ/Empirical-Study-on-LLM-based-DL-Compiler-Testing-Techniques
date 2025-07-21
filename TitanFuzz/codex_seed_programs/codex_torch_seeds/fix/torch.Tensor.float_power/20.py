'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.float_power\ntorch.Tensor.float_power(_input_tensor, exponent)\n'
import torch
input_tensor = torch.tensor([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
output_tensor = input_tensor.float_power(2)
print(output_tensor)