input_tensor = torch.rand(3, 3, requires_grad=True)
input2 = torch.rand(3, 3, requires_grad=True)
torch.Tensor.cholesky_solve(input_tensor, input2, upper=False)