'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.masked_fill_\ntorch.Tensor.masked_fill_(_input_tensor, mask, value\n'
import torch
input_tensor = torch.randint(0, 10, (3, 3))
mask = torch.tensor([[0, 0, 1], [0, 1, 0], [1, 0, 0]], dtype=torch.bool)
value = torch.tensor(100)
result = torch.Tensor.masked_fill_(input_tensor, mask, value)
print(result)