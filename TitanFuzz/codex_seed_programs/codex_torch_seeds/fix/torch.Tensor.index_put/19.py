'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.index_put\ntorch.Tensor.index_put(_input_tensor, indices, values, accumulate=False)\n'
import torch
input_tensor = torch.rand(10, 10)
indices = torch.tensor([[0, 0], [0, 1], [1, 0], [1, 1], [2, 2], [3, 3], [4, 4], [5, 5], [6, 6], [7, 7], [8, 8], [9, 9]])
values = torch.tensor([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
input_tensor.index_put(indices, values, accumulate=False)
print(input_tensor)