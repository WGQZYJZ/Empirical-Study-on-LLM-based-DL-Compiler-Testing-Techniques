'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.index_fill_\ntorch.Tensor.index_fill_(_input_tensor, dim, index, value)\n'
import torch
input_tensor = torch.tensor([[0, 1, 2, 3], [4, 5, 6, 7], [8, 9, 10, 11]], dtype=torch.float32)
print('input_tensor:', input_tensor)
index = torch.tensor([0, 2], dtype=torch.long)
value = torch.tensor(100, dtype=torch.float32)
input_tensor.index_fill_(dim=0, index=index, value=value)
print('input_tensor after index_fill_:', input_tensor)