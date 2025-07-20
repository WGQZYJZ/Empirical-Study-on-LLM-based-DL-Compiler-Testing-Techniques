input_tensor = torch.randn(3, 3)
input_tensor = input_tensor.mm(input_tensor.t())
input2 = torch.randn(3, 2)
cholesky_solve = torch.Tensor.cholesky_solve(input_tensor, input2, upper=False)