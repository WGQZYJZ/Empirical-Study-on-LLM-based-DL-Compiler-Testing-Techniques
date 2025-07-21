'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.bitwise_left_shift\ntorch.Tensor.bitwise_left_shift(_input_tensor, other)\n'
import torch
input_tensor = torch.randint(low=0, high=10, size=(2, 3), dtype=torch.int32)
output_tensor = input_tensor.bitwise_left_shift(2)
print('input_tensor: ', input_tensor)
print('output_tensor: ', output_tensor)