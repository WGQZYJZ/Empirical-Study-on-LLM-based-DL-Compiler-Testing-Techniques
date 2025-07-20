input_tensor = torch.randn(3, 3)
output_tensor = torch.Tensor.exponential_(input_tensor, lambd=1, generator=None)