'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.true_divide\ntorch.Tensor.true_divide(_input_tensor, value)\n'
import torch
input_tensor = torch.rand(1, 2, 3, 4)
output_tensor = torch.Tensor.true_divide(input_tensor, 2)
print(output_tensor)