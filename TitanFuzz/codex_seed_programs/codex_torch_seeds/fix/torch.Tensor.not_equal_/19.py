'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.not_equal_\ntorch.Tensor.not_equal_(_input_tensor, other)\n'
import torch
input_tensor = torch.tensor([[1, 2, 3], [4, 5, 6]], dtype=torch.float)
other = torch.tensor([[1, 2, 3], [4, 5, 6]], dtype=torch.float)
torch.Tensor.not_equal_(input_tensor, other)
print(input_tensor)