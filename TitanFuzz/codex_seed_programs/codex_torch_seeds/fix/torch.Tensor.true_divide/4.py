'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.true_divide\ntorch.Tensor.true_divide(_input_tensor, value)\n'
import torch
input_tensor = torch.randn(2, 3)
value = 2
output_tensor = torch.Tensor.true_divide(input_tensor, value)
print(output_tensor)