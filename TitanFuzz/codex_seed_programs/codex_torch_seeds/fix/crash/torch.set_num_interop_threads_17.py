'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.set_num_interop_threads\ntorch.set_num_interop_threads(int)\n'
import torch
import time
import numpy as np
torch.set_num_interop_threads(1)
input_data = torch.randn(1, 1, 28, 28)
torch.set_num_interop_threads(1)
start_time = time.time()
output_data = torch.conv2d(input_data, torch.randn(1, 1, 3, 3), padding=1)
end_time = time.time()
print('The running time is: ', (end_time - start_time))