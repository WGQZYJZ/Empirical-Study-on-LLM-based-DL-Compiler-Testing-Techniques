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