'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.resolve_neg\ntorch.Tensor.resolve_neg(_input_tensor)\n'
import torch
input_tensor = torch.Tensor([[1, 2, 3], [4, 5, 6]])
output_tensor = torch.Tensor.resolve_neg(input_tensor)
print(input_tensor)
print(output_tensor)