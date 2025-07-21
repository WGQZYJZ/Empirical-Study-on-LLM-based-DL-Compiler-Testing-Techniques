'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.masked_fill_\ntorch.Tensor.masked_fill_(_input_tensor, mask, value\n'
import torch
input_tensor = torch.randint(low=0, high=10, size=(5, 5))
mask = torch.tensor([[1, 1, 1, 0, 0], [1, 0, 1, 0, 0], [0, 0, 1, 0, 0], [0, 0, 1, 0, 0], [0, 0, 1, 0, 0]], dtype=torch.uint8)
input_tensor.masked_fill_(mask, 0)
print(input_tensor)