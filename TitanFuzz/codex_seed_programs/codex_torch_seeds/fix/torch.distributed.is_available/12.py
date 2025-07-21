'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.distributed.is_available\ntorch.distributed.is_available()\n'
import torch
print(torch.cuda.is_available())
print(torch.distributed.is_available())
print(torch.distributed.is_initialized())
if torch.distributed.is_available():
    print('Distributed package is available')
else:
    print('Distributed package is NOT available')