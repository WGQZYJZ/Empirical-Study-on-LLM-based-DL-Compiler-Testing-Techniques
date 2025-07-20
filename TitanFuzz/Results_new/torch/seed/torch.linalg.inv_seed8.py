A = torch.randn(3, 3)
A.requires_grad_(True)
invA = torch.linalg.inv(A)