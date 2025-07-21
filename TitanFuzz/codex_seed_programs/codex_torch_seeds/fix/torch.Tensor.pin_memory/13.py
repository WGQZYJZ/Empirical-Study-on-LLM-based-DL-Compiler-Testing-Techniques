'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.pin_memory\ntorch.Tensor.pin_memory(_input_tensor)\n'
import torch
import time
_input_tensor = torch.rand(size=(1000, 1000))
start_time = time.time()
_input_tensor.pin_memory()
print(('--- %s seconds ---' % (time.time() - start_time)))