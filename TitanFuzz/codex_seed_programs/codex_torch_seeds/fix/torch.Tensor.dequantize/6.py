'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.dequantize\ntorch.Tensor.dequantize(_input_tensor)\n'
import torch
input_tensor = torch.tensor([[0, 1, 2, 3], [4, 5, 6, 7]])
scale = 1.0
zero_point = 0
output_tensor = torch.Tensor.dequantize(input_tensor)
print(output_tensor)