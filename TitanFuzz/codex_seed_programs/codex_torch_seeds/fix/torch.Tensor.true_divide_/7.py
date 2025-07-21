'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.true_divide_\ntorch.Tensor.true_divide_(_input_tensor, value)\n'
import torch
input_tensor = torch.tensor([[1, 2, 3, 4], [2, 3, 4, 5]])
value = 2
torch.Tensor.true_divide_(input_tensor, value)
print(input_tensor)