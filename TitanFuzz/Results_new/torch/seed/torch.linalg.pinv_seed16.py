A = torch.randn(3, 3, requires_grad=True)
pinv_A = torch.linalg.pinv(A)
A = torch.randn(3, 3, requires_grad=True)
inv_A = torch.inverse(A)
A = torch.randn(3, 3, requires_grad=True)
eig_A = torch.eig(A)