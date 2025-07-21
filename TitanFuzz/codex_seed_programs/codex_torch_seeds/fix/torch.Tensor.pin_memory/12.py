'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.pin_memory\ntorch.Tensor.pin_memory(_input_tensor)\n'
import torch
import time
_input_tensor = torch.rand(10000, 10000)
start = time.time()
_input_tensor_pinned = _input_tensor.pin_memory()
end = time.time()
print('Time cost: ', (end - start))
print('The type of _input_tensor_pinned: ', type(_input_tensor_pinned))