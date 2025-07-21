'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.range\ntorch.range(start=0, end, step=1, *, out=None, dtype=None, layout=torch.strided, device=None, requires_grad=False)\n'
import torch
print('\nTask 1: import PyTorch')
print('PyTorch version: ', torch.__version__)
print('PyTorch location: ', torch.__file__)
print('PyTorch is compiled with CUDA: ', torch.cuda.is_available())
print('PyTorch is compiled with MKL: ', torch.backends.mkl.is_available())
print('PyTorch is compiled with MKLDNN: ', torch.backends.mkldnn.is_available())
print('\nTask 2: Generate input data')
start = 0
end = 10
step = 1
print('Start: ', start)
print('End: ', end)
print('Step: ', step)
print('\nTask 3: Call the API torch.range')
print(torch.range(start, end, step))