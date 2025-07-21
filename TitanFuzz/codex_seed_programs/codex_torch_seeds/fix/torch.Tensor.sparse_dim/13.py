'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.sparse_dim\ntorch.Tensor.sparse_dim(_input_tensor)\n'
import torch
data = [[1, 2, 3], [4, 5, 6]]
_input_tensor = torch.Tensor(data)
output_tensor = torch.Tensor.sparse_dim(_input_tensor)
print(output_tensor)