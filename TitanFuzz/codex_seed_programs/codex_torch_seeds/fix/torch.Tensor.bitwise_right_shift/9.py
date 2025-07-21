'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.bitwise_right_shift\ntorch.Tensor.bitwise_right_shift(_input_tensor, other)\n'
import torch
input_tensor = torch.randint(low=0, high=100, size=(1,), dtype=torch.int32)
output_tensor = torch.Tensor.bitwise_right_shift(input_tensor, 1)
print('Bitwise right shift of input tensor: ', input_tensor)
print('Result of bitwise right shift: ', output_tensor)