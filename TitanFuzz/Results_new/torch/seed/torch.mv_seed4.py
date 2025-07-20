input = torch.randn(2, 3)
vec = torch.tensor([1, 0, (- 1)], dtype=torch.float)
torch.mv(input, vec)