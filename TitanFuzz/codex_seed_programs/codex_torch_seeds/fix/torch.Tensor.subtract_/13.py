'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.subtract_\ntorch.Tensor.subtract_(_input_tensor, other, *, alpha=1)\n'
import torch
input_tensor = torch.tensor([1.0, 2.0, 3.0, 4.0, 5.0])
other_tensor = torch.tensor([2.0, 2.0, 2.0, 2.0, 2.0])
output_tensor = torch.Tensor.subtract_(input_tensor, other_tensor)
print(output_tensor)