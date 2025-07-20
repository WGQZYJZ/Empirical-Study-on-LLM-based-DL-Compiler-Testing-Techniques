A = torch.randn(3, 3)
A_inv = torch.linalg.inv_ex(A)
A_inv_np = np.linalg.inv(A.numpy())