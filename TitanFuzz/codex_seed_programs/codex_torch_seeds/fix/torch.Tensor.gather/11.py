'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.gather\ntorch.Tensor.gather(_input_tensor, dim, index)\n'
import torch
input_tensor = torch.tensor([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print('input_tensor: ', input_tensor)
result = torch.Tensor.gather(input_tensor, dim=1, index=torch.tensor([[0, 1], [1, 2], [2, 0]]))
print('result: ', result)