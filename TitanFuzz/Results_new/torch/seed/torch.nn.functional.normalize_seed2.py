input = torch.randn(4, 5)
output = torch.nn.functional.normalize(input, p=2.0, dim=1, eps=1e-12, out=None)