A = torch.tensor([[1, 2], [3, 4]], dtype=torch.float)
A2 = torch.linalg.matrix_power(A, 2)
A3 = torch.linalg.matrix_power(A, 3)
A4 = torch.linalg.matrix_power(A, 4)
A5 = torch.linalg.matrix_power(A, 5)