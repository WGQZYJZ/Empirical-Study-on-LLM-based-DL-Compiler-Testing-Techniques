'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.bitwise_right_shift\ntorch.Tensor.bitwise_right_shift(_input_tensor, other)\n'
import torch
import torch
input_tensor = torch.randint(low=0, high=128, size=(3, 4), dtype=torch.int8)
output_tensor = torch.Tensor.bitwise_right_shift(input_tensor, other=1)
print('input_tensor: ', input_tensor)
print('output_tensor: ', output_tensor)