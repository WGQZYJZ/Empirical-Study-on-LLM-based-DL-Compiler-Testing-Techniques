'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.index_put\ntorch.Tensor.index_put(_input_tensor, indices, values, accumulate=False)\n'
import torch
input_tensor = torch.randint(0, 10, (3, 3))
print(input_tensor)
indices = torch.tensor([[0, 0], [1, 1], [2, 2]])
values = torch.tensor([1, 2, 3])
input_tensor.index_put((indices, values), accumulate=False)
print(input_tensor)
indices = torch.tensor([[0, 0], [1, 1], [2, 2]])
values = torch.tensor([1, 2, 3])
input_tensor.index_put((indices, values), accumulate=True)
print(input_tensor)