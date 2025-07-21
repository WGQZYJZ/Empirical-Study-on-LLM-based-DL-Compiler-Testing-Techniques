'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.dequantize\ntorch.dequantize(tensors)\n'
import torch
tensors = torch.randint(0, 256, (2, 2), dtype=torch.uint8)
tensors = tensors.float()
print('tensors: ', tensors)
result = torch.dequantize(tensors)
print('result: ', result)