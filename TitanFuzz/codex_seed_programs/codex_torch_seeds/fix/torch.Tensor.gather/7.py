'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.gather\ntorch.Tensor.gather(_input_tensor, dim, index)\n'
import torch
input_tensor = torch.Tensor([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
index = torch.tensor([0, 1, 2])
result = torch.Tensor.gather(input_tensor, 1, index)
print(result)