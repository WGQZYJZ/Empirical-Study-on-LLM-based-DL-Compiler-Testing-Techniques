'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.dequantize\ntorch.Tensor.dequantize(_input_tensor)\n'
import torch
import torch
input_tensor = torch.randint(0, 256, (1, 3, 10, 10), dtype=torch.uint8)
output_tensor = torch.Tensor.dequantize(input_tensor)
print('input tensor: ', input_tensor)
print('output tensor: ', output_tensor)