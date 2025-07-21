'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.dequantize\ntorch.dequantize(tensors)\n'
import torch
tensors = torch.quantize_per_tensor(torch.randn(5, 5).float(), scale=0.5, zero_point=5, dtype=torch.quint8)
torch.dequantize(tensors)