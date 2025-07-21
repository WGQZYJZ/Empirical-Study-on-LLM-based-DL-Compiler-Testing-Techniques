'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.hsplit\ntorch.Tensor.hsplit(_input_tensor, split_size_or_sections)\n'
import torch
input_tensor = torch.randn(3, 5)
print(input_tensor.hsplit(2))
print(input_tensor.hsplit(torch.LongTensor([1, 3])))
print(input_tensor.hsplit(torch.LongTensor([1, 3]), dim=1))