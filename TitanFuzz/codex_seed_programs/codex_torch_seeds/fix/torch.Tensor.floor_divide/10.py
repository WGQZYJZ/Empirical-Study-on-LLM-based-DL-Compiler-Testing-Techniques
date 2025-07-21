'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.floor_divide\ntorch.Tensor.floor_divide(_input_tensor, value)\n'
import torch
input_tensor = torch.arange(0, 10, dtype=torch.float32)
output_tensor = torch.Tensor.floor_divide(input_tensor, 2)
print(output_tensor)