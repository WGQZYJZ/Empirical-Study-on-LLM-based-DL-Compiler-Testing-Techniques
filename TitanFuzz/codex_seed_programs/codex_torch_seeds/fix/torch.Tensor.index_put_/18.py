'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.index_put_\ntorch.Tensor.index_put_(_input_tensor, indices, values, accumulate=False)\n'
import torch
input_tensor = torch.rand((3, 3))
print(input_tensor)
indices = torch.LongTensor([[0, 1], [1, 2]])
values = torch.Tensor([1, 2])
input_tensor.index_put_(indices, values, accumulate=False)
print(input_tensor)
indices = torch.LongTensor([[0, 1], [1, 2]])
values = torch.Tensor([1, 2])
input_tensor.index_put_(indices, values, accumulate=True)
print(input_tensor)