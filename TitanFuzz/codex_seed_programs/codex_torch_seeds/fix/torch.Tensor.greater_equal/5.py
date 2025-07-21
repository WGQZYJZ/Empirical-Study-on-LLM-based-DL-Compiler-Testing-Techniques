'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.greater_equal\ntorch.Tensor.greater_equal(_input_tensor, other)\n'
import torch
input_tensor = torch.tensor([1.0, 2.0, 3.0, 4.0, 5.0])
other = torch.tensor([1.0, 2.0, 3.0, 4.0, 5.0])
output_tensor = torch.Tensor.greater_equal(input_tensor, other)
print(output_tensor)