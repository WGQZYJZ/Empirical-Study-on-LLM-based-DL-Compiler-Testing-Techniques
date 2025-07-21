'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.pin_memory\ntorch.Tensor.pin_memory(_input_tensor)\n'
import torch
import time
_input_tensor = torch.randn(1, 3, 224, 224)
time_start = time.time()
_input_tensor.pin_memory()
time_end = time.time()
print('Time cost: {}'.format((time_end - time_start)))