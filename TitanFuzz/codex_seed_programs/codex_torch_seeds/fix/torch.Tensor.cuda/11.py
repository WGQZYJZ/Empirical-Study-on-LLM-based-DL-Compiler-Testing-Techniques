'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.cuda\ntorch.Tensor.cuda(_input_tensor, device=None, non_blocking=False, memory_format=torch.preserve_format)\n'
import torch
import time
input_tensor = torch.rand(10000, 1000)
start_time = time.time()
output_tensor = input_tensor.cuda()
end_time = time.time()
print('time cost:', (end_time - start_time))