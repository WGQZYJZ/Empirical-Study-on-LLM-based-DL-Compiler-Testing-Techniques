A = torch.randn(3, 3)
det = torch.linalg.det(A)
log_det = torch.linalg.slogdet(A)