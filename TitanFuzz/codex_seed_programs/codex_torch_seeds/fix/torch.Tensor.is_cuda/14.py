'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.is_cuda\ntorch.Tensor.is_cuda(_input_tensor, )\n'
import torch
input_tensor = torch.FloatTensor([[1, 2, 3], [4, 5, 6]])
print(input_tensor)
print(torch.Tensor.is_cuda(input_tensor))