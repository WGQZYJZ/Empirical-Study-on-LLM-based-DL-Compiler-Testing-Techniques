A = torch.tensor([[1, 2, 3], [4, 5, 6], [7, 8, 9]], dtype=torch.float64)
tau = torch.tensor([1], dtype=torch.float64)
torch.linalg.householder_product(A, tau)