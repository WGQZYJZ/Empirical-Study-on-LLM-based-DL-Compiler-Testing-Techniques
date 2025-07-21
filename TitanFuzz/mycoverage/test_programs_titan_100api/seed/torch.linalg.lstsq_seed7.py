A = torch.tensor([[1, 2], [3, 4]], dtype=torch.float)
B = torch.tensor([[5, 6], [7, 8]], dtype=torch.float)
X = torch.linalg.lstsq(A, B)