'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.bitwise_left_shift\ntorch.Tensor.bitwise_left_shift(_input_tensor, other)\n'
import torch
import torch
input_tensor = torch.tensor([1, 2, 3, 4], dtype=torch.int32)
result = torch.Tensor.bitwise_left_shift(input_tensor, 2)
print(result)