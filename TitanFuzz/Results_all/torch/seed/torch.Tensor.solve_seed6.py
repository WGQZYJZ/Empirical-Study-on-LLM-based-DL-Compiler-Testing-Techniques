input_tensor = torch.randn(2, 3, requires_grad=True)
A = torch.randn(3, 3)
torch.Tensor.solve(input_tensor, A)