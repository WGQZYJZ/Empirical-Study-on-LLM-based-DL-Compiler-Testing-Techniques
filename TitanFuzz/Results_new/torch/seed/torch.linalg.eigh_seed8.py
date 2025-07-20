A = torch.tensor([[1, 2, 3], [4, 5, 6], [7, 8, 9]], dtype=torch.float)
(eig_val, eig_vec) = torch.linalg.eigh(A)