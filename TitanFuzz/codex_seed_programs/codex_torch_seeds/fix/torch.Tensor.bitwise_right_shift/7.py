'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.bitwise_right_shift\ntorch.Tensor.bitwise_right_shift(_input_tensor, other)\n'
import torch
input_tensor = torch.tensor([[1, 2, 3], [4, 5, 6]], dtype=torch.int32)
print('Input tensor: ', input_tensor)
output_tensor = torch.Tensor.bitwise_right_shift(input_tensor, 1)
print('Output tensor: ', output_tensor)