A = torch.tensor([[1.0, 2.0, 3.0], [4.0, 5.0, 6.0], [7.0, 8.0, 9.0]])
tau = torch.tensor([0.5])
h_A = torch.linalg.householder_product(A, tau)