'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.frombuffer\ntorch.frombuffer(buffer, *, dtype, count=-1, offset=0, requires_grad=False)\n'
import torch
buffer = bytearray(4)
buffer[0] = 1
buffer[1] = 2
buffer[2] = 3
buffer[3] = 4
buffer_tensor = torch.frombuffer(buffer, dtype=torch.int8)
print(buffer_tensor)
buffer_tensor = torch.frombuffer(buffer, dtype=torch.int8, count=3)
print(buffer_tensor)
buffer_tensor = torch.frombuffer(buffer, dtype=torch.int8, count=3, offset=1)
print(buffer_tensor)