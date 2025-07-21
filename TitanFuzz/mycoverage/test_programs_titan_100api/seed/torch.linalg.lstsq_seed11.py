A = torch.tensor([[1.0, 2.0], [3.0, 4.0]])
b = torch.tensor([[1.0], [2.0]])
x = torch.linalg.lstsq(A, b)