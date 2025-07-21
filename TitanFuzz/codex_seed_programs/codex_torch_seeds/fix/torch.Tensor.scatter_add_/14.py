'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.scatter_add_\ntorch.Tensor.scatter_add_(_input_tensor, dim, index, src)\n'
import torch
input_tensor = torch.tensor([[1, 2, 3], [4, 5, 6], [7, 8, 9]], dtype=torch.float32)
index = torch.tensor([0, 2, 1], dtype=torch.long)
src = torch.tensor([[10, 11, 12], [13, 14, 15], [16, 17, 18]], dtype=torch.float32)
input_tensor.scatter_add_(dim=0, index=index, src=src)
print(input_tensor)
'\nExpected output:\ntensor([[17., 19., 21.],\n        [ 4.,  5.,  6.],\n        [23., 25., 27.]])\n'