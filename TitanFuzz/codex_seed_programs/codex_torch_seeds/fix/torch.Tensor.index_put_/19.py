'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.index_put_\ntorch.Tensor.index_put_(_input_tensor, indices, values, accumulate=False)\n'
import torch
tensor = torch.randn(2, 3)
indices = torch.LongTensor([[0, 0], [1, 2]])
values = torch.FloatTensor([3, 4])
tensor.index_put_(indices, values, accumulate=False)
print(tensor)