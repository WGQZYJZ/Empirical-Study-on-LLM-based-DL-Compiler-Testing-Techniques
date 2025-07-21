'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.record_stream\ntorch.Tensor.record_stream(_input_tensor, stream\n'
import torch
import numpy as np
import time
import torch
import numpy as np
input_tensor = torch.randn(100, 100)
torch.cuda.synchronize()
start = time.time()
torch.Tensor.record_stream(input_tensor, torch.cuda.current_stream())
torch.cuda.synchronize()
end = time.time()
print('Time: {} ms'.format(((end - start) * 1000)))