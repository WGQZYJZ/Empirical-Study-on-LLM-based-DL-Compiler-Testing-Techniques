input_data = torch.randn(3, 3)
output_data = torch.Tensor.exponential_(input_data, lambd=1)