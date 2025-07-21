'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.fft.fftn\ntorch.fft.fftn(input, s=None, dim=None, norm=None, *, out=None)\n'
import torch
import time
input_size = (8, 16, 16, 16)
input_data = torch.randn(*input_size)
start = time.time()
output = torch.fft.fftn(input_data, norm='ortho')
end = time.time()
print('torch.fft.fftn: {}'.format((end - start)))