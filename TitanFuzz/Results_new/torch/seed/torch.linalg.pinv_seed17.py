A = torch.tensor([[1.0, 2.0, 3.0], [4.0, 5.0, 6.0], [7.0, 8.0, 9.0]])
A_inv = torch.linalg.pinv(A)
A_dot_A_inv = torch.mm(A, A_inv)
A_inv_dot_A = torch.mm(A_inv, A)