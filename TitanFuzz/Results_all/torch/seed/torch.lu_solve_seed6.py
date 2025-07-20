A = torch.tensor([[1, 2, 3], [4, 5, 6], [7, 8, 9]], dtype=torch.float)
b = torch.tensor([[1], [2], [3]], dtype=torch.float)
(lu_data, lu_pivots) = torch.lu(A)
x = torch.lu_solve(b, lu_data, lu_pivots)