'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.reciprocal\ntorch.Tensor.reciprocal(_input_tensor)\n'
import torch
input_tensor = torch.tensor([1.0, 2.0, 3.0])
output_tensor = torch.Tensor.reciprocal(input_tensor)
print(output_tensor)