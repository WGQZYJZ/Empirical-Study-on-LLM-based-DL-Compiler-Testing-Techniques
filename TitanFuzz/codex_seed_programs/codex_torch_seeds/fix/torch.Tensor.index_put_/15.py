'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.index_put_\ntorch.Tensor.index_put_(_input_tensor, indices, values, accumulate=False)\n'
import torch
input_tensor = torch.randn(3, 3)
print(input_tensor)
indices = torch.tensor([[0, 1], [1, 2]])
values = torch.tensor([3, 4], dtype=torch.float32)
input_tensor.index_put_(indices, values, accumulate=False)
print(input_tensor)