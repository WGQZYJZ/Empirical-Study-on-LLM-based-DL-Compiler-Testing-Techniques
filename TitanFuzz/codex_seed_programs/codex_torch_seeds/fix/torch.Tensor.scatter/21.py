'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.scatter\ntorch.Tensor.scatter(_input_tensor, dim, index, src)\n'
import torch
import torch
input_tensor = torch.Tensor([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print('Input tensor: \n', input_tensor)
result_tensor = input_tensor.scatter(dim=0, index=torch.LongTensor([[0, 1], [1, 2]]), src=torch.Tensor([[1, 2], [3, 4]]))
print('Result tensor: \n', result_tensor)