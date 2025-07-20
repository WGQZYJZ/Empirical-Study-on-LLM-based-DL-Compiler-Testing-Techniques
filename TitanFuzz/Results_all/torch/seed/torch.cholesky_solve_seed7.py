input_data = torch.rand(3, 3, device='cpu', dtype=torch.float64)
input_data2 = torch.rand(3, 3, device='cpu', dtype=torch.float64)
output = torch.cholesky_solve(input_data, input_data2)