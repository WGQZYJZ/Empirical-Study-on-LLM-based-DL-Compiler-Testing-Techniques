'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.scatter_add_\ntorch.Tensor.scatter_add_(_input_tensor, dim, index, src)\n'
import torch
input_tensor = torch.Tensor([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
index_tensor = torch.LongTensor([[0, 1, 2], [1, 2, 0]])
src_tensor = torch.Tensor([[10, 11, 12], [13, 14, 15]])
output_tensor = torch.Tensor([[0, 0, 0], [0, 0, 0], [0, 0, 0]])
output_tensor.scatter_add_(dim=0, index=index_tensor, src=src_tensor)
print(output_tensor)