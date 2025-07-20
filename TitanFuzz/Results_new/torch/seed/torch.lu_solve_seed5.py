A = torch.rand(3, 3, dtype=torch.float64)
b = torch.rand(3, 1, dtype=torch.float64)
(LU_data, LU_pivots) = torch.lu(A)
x = torch.lu_solve(b, LU_data, LU_pivots)