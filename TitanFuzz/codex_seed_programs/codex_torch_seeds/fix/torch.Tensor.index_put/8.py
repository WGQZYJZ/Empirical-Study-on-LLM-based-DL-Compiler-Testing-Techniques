'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.index_put\ntorch.Tensor.index_put(_input_tensor, indices, values, accumulate=False)\n'
import torch
import torch
input_tensor = torch.randint(0, 10, [3, 3, 3])
indices = torch.tensor([[0, 1, 2], [0, 1, 2], [0, 1, 2]])
values = torch.tensor([1, 2, 3])
input_tensor.index_put((indices, indices, indices), values)
print(input_tensor)