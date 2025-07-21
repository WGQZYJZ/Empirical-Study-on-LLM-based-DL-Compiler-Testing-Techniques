'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.index_put\ntorch.Tensor.index_put(_input_tensor, indices, values, accumulate=False)\n'
import torch
input_tensor = torch.randn(4, 4)
indices = torch.tensor([[0, 0], [1, 1], [2, 2], [3, 3]])
values = torch.tensor([1, 2, 3, 4])
output_tensor = input_tensor.index_put((indices, values))
print(output_tensor)