x = torch.tensor([1, 2, 3, 4], dtype=torch.float32)
y = torch.pow(x, 2)
out = torch.empty(4)
torch.pow(x, 2, out=out)