'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.index_put_\ntorch.Tensor.index_put_(_input_tensor, indices, values, accumulate=False)\n'
import torch
input_tensor = torch.Tensor([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
torch.Tensor.index_put_(input_tensor, torch.LongTensor([[0, 0], [1, 1], [2, 2]]), torch.Tensor([[10, 20, 30], [40, 50, 60], [70, 80, 90]]), accumulate=False)
print('The result is: ', input_tensor)