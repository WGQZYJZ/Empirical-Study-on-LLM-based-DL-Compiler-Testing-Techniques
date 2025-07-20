a = torch.tensor([[1, 2], [3, 4]], dtype=torch.float32)
b = torch.tensor([[5, 6], [7, 8]], dtype=torch.float32)
c = torch.tensor([[0, 0], [0, 0]], dtype=torch.float32)
torch.kron(a, b, out=c)