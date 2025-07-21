'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.dequantize\ntorch.Tensor.dequantize(_input_tensor)\n'
import torch
import torch
input_tensor = torch.randint(0, 255, (2, 3, 4, 5), dtype=torch.uint8)
print('input_tensor:', input_tensor)
output_tensor = torch.Tensor.dequantize(input_tensor)
print('output_tensor:', output_tensor)