A = torch.randn(3, 3, dtype=torch.float64, requires_grad=True)
invA = torch.linalg.inv_ex(A)