'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.pin_memory\ntorch.Tensor.pin_memory(_input_tensor)\n'
import torch
import time
print('PyTorch version: ', torch.__version__)
_input_tensor = torch.rand(size=(1000, 1000, 1000), dtype=torch.float32)
start_time = time.time()
_input_tensor = _input_tensor.pin_memory()
end_time = time.time()
print(('Time cost of torch.Tensor.pin_memory(): %f sec' % (end_time - start_time)))