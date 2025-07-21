dtype = torch.float
device = torch.device('cpu')
N = 10
A = torch.randn(N, N, dtype=dtype, device=device)
A = A.mm(A.t())
eigvals = torch.linalg.eigvalsh(A)