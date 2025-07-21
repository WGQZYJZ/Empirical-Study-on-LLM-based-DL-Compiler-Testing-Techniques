'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.dequantize\ntorch.Tensor.dequantize(_input_tensor)\n'
import torch
input_tensor = torch.randint(0, 255, (2, 3, 3), dtype=torch.uint8)
scale = torch.tensor(0.1)
zero_point = torch.tensor(0)
output_tensor = torch.Tensor.dequantize(input_tensor, scale, zero_point)
print('input_tensor = ', input_tensor)
print('output_tensor = ', output_tensor)