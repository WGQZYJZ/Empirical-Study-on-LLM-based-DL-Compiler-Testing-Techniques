'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.take\ntorch.Tensor.take(_input_tensor, indices)\n'
import torch
input_data = torch.randn(5, 5)
indices = torch.LongTensor([[0, 1], [2, 3]])
print(torch.Tensor.take(input_data, indices))