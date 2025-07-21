'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.randn\ntorch.randn(*size, *, out=None, dtype=None, layout=torch.strided, device=None, requires_grad=False)\n'
import torch
dtype = torch.float
device = torch.device('cpu')
(N, D_in, H, D_out) = (64, 1000, 100, 10)
x = torch.randn(N, D_in, device=device, dtype=dtype)
y = torch.randn(N, D_out, device=device, dtype=dtype)
w1 = torch.randn(D_in, H, device=device, dtype=dtype)
w2 = torch.randn(H, D_out, device=device, dtype=dtype)
learning_rate = 1e-06
for t in range(500):
    h = x.mm(w1)