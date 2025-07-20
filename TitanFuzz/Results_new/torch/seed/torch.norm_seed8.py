input = torch.randn(3, 5)
output = torch.norm(input, p=2, dim=1, keepdim=False, out=None, dtype=None)