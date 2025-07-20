A = torch.tensor([[1, 2, 3], [4, 5, 6], [7, 8, 9]], dtype=torch.float)
(w, v) = torch.linalg.eigh(A)
A_inv = torch.inverse(A)
I = torch.matmul(A, A_inv)