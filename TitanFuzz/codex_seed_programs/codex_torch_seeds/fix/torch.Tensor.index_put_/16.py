'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.index_put_\ntorch.Tensor.index_put_(_input_tensor, indices, values, accumulate=False)\n'
import torch
import numpy as np
input_tensor = torch.Tensor(np.array([[1, 2, 3], [4, 5, 6]]))
indices = torch.LongTensor([[0, 1], [1, 2]])
values = torch.Tensor([7, 8])
input_tensor.index_put_(indices, values, accumulate=False)
print(input_tensor)