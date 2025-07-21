'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.resolve_neg\ntorch.Tensor.resolve_neg(_input_tensor)\n'
import torch
input_data = torch.Tensor([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])
print(input_data)
resolved_data = torch.Tensor.resolve_neg(input_data)
print(resolved_data)