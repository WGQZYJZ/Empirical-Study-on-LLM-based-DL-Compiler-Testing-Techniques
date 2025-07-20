A = torch.randn(3, 3, 3)
result = torch.linalg.vector_norm(A, ord=2, dim=None, keepdim=False, dtype=None, out=None)