'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.dequantize\ntorch.Tensor.dequantize(_input_tensor)\n'
import torch
input_tensor = torch.randint(low=0, high=255, size=(1, 3, 3, 3), dtype=torch.uint8)
print('input_tensor: ', input_tensor)
dequantized_tensor = torch.Tensor.dequantize(input_tensor)
print('dequantized_tensor: ', dequantized_tensor)