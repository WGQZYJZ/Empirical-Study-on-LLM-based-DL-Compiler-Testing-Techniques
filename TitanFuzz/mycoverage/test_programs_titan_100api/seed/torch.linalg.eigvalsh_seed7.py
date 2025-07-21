A = torch.tensor([[1, 2, 3], [4, 5, 6], [7, 8, 9]], dtype=torch.float32)
eigvalsh = torch.linalg.eigvalsh(A)
eigvalsh = torch.linalg.eigvalsh(A, UPLO='U')
eigvalsh = torch.linalg.eigvalsh(A, UPLO='L')