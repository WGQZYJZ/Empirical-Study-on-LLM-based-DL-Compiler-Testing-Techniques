A = torch.rand(2, 3, dtype=torch.float, requires_grad=True)
B = torch.rand(2, 3, dtype=torch.float, requires_grad=True)
torch.linalg.lstsq(A, B)