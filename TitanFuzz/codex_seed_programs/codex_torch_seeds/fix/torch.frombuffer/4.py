'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.frombuffer\ntorch.frombuffer(buffer, *, dtype, count=-1, offset=0, requires_grad=False)\n'
import torch
data = bytearray([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
tensor = torch.frombuffer(data, dtype=torch.int8, count=5, offset=3)
print(tensor)