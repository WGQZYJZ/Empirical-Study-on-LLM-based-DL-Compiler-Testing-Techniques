'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.dequantize\ntorch.dequantize(tensors)\n'
import torch
import torch
input_tensor = torch.randint(0, 256, (2, 2), dtype=torch.uint8, device='cpu')
print(input_tensor)
output_tensor = torch.dequantize(input_tensor)
print(output_tensor)