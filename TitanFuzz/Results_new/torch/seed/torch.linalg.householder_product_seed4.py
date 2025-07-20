A = torch.rand(4, 4)
tau = torch.rand(4)
torch.linalg.householder_product(A, tau)