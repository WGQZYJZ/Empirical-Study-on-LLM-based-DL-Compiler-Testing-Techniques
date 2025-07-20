input_tensor = torch.randn(4, 4)
exponential_tensor = torch.Tensor.exponential_(input_tensor, lam=1, generator=None)