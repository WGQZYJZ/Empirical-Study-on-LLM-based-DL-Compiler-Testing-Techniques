'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.scatter_add_\ntorch.Tensor.scatter_add_(_input_tensor, dim, index, src)\n'
import torch
import torch
input_tensor = torch.randint(0, 10, (1, 10))
print('input_tensor: ', input_tensor)
index = torch.tensor([[4, 5, 6, 7], [3, 3, 3, 3]], dtype=torch.long)
print('index: ', index)
src = torch.tensor([3, 4, 5, 6], dtype=torch.float)
print('src: ', src)
output_tensor = torch.Tensor.scatter_add_(input_tensor, dim=0, index=index, src=src)
print('output_tensor: ', output_tensor)