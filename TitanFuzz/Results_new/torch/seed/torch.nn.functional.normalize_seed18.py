input = torch.randn(2, 3)
normalized_input = torch.nn.functional.normalize(input, p=2.0, dim=1, eps=1e-12, out=None)