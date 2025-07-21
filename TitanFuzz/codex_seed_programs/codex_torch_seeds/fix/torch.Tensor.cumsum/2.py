'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.cumsum\ntorch.Tensor.cumsum(_input_tensor, dim, dtype=None)\n'
import torch
input_tensor = torch.tensor([[1.0, 2.0, 3.0], [4.0, 5.0, 6.0]])
cumsum_tensor = input_tensor.cumsum(dim=1)
print(cumsum_tensor)