'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.dequantize\ntorch.dequantize(tensors)\n'
import torch
input_tensor = torch.randint(0, 256, (1, 2, 3, 4), dtype=torch.uint8)
output = torch.dequantize(input_tensor)
print(output)