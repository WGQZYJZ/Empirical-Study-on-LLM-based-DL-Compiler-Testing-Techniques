'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.bitwise_not\ntorch.Tensor.bitwise_not(_input_tensor)\n'
import torch
input_tensor = torch.Tensor([[1, 0, 1], [0, 1, 0], [1, 0, 1]])
print(torch.Tensor.bitwise_not(input_tensor))