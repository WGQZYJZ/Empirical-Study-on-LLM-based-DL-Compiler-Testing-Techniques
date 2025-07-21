'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.index_put_\ntorch.Tensor.index_put_(_input_tensor, indices, values, accumulate=False)\n'
import torch
_input_tensor = torch.Tensor([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
indices = torch.LongTensor([[0, 1], [1, 2]])
values = torch.Tensor([[10, 20], [30, 40]])
torch.Tensor.index_put_(_input_tensor, indices, values, accumulate=True)
print(_input_tensor)