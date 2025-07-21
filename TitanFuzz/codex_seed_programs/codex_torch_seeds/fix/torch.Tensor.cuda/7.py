'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.cuda\ntorch.Tensor.cuda(_input_tensor, device=None, non_blocking=False, memory_format=torch.preserve_format)\n'
import torch
import time
input_tensor = torch.randn(10000, 10000).cuda()
start = time.time()
output_tensor = torch.Tensor.cuda(input_tensor)
end = time.time()
print('time:', (end - start))