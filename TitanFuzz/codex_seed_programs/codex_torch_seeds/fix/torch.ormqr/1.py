'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.ormqr\ntorch.ormqr(input, tau, other, left=True, transpose=False, *, out=None)\n'
import torch
print('Task 1: import PyTorch')
print('PyTorch version:', torch.__version__)
print('CUDA available:', torch.cuda.is_available())
print('cuDNN enabled:', torch.backends.cudnn.enabled)
print('Task 2: Generate input data')
input = torch.randn(3, 5, dtype=torch.float32, device='cuda')
tau = torch.randn(3, dtype=torch.float32, device='cuda')
other = torch.randn(3, 5, dtype=torch.float32, device='cuda')
print('Task 3: Call the API torch.ormqr')
output = torch.ormqr(input, tau, other, left=True, transpose=False)
print('output:', output)