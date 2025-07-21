'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.bitwise_right_shift\ntorch.Tensor.bitwise_right_shift(_input_tensor, other)\n'
import torch
input_tensor = torch.randint(low=0, high=2, size=(5, 5), dtype=torch.int8)
other = torch.tensor([1, 2, 3, 4, 5])
result = input_tensor.bitwise_right_shift(other)
print(input_tensor)
print(result)