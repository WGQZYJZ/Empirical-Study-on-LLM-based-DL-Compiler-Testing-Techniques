input_tensor = torch.randn(1, 3)
output_tensor = torch.Tensor.exponential_(input_tensor, lambd=1)