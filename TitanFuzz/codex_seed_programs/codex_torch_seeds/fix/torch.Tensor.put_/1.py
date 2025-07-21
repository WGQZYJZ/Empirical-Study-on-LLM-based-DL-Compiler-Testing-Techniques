'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.put_\ntorch.Tensor.put_(_input_tensor, index, source, accumulate=False)\n'
import torch
input_tensor = torch.Tensor([[1, 2, 3], [4, 5, 6]])
index = torch.LongTensor([[0, 1], [1, 2]])
source = torch.Tensor([[7, 8], [9, 10]])
input_tensor.put_(index, source)
print(input_tensor)
index = torch.LongTensor([[0, 1], [1, 2]])
source = torch.Tensor([[7, 8], [9, 10]])
input_tensor.put_(index, source, accumulate=True)
print(input_tensor)