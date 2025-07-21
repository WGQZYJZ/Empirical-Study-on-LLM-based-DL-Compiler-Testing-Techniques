'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.bitwise_right_shift\ntorch.Tensor.bitwise_right_shift(_input_tensor, other)\n'
import torch
input_tensor = torch.randint(0, 2, (3, 3), dtype=torch.uint8)
output_tensor = input_tensor.bitwise_right_shift(1)
print('input_tensor: ', input_tensor)
print('output_tensor: ', output_tensor)