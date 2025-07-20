input = torch.randn(3, 5, dtype=torch.float, requires_grad=True)
rank = torch.matrix_rank(input)