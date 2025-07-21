'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.pin_memory\ntorch.Tensor.pin_memory(_input_tensor)\n'
import torch
import time
input_tensor = torch.randn(1000, 1000)
input_tensor = input_tensor.pin_memory()
print(torch.cuda.memory_allocated())
print(torch.cuda.memory_cached())
print(torch.cuda.max_memory_allocated())
print(torch.cuda.max_memory_cached())
torch.cuda.empty_cache()