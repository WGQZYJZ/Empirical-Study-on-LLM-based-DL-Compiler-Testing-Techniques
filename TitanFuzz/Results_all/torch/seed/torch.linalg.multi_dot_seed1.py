A = torch.randn(3, 3, requires_grad=True)
B = torch.randn(3, 3, requires_grad=True)
C = torch.randn(3, 3, requires_grad=True)
D = torch.linalg.multi_dot([A, B, C])