input = torch.randn(3, 4, dtype=torch.float32)
norm = torch.nn.functional.normalize(input, p=2.0, dim=1, eps=1e-12)