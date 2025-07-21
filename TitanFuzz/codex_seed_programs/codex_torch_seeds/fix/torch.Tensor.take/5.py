'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.take\ntorch.Tensor.take(_input_tensor, indices)\n'
import torch
import torch
input_tensor = torch.Tensor([[1, 2, 3], [4, 5, 6]])
indices = torch.LongTensor([0, 2])
output_tensor = torch.Tensor.take(input_tensor, indices)
print(output_tensor)