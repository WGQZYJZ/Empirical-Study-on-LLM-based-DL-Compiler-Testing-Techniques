'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.bitwise_not_\ntorch.Tensor.bitwise_not_(_input_tensor)\n'
import torch
import torch
input_tensor = torch.tensor([[0, 0, 1, 1], [1, 0, 1, 0], [0, 1, 1, 0], [1, 1, 1, 1]], dtype=torch.uint8)
result = torch.Tensor.bitwise_not_(input_tensor)
print(result)