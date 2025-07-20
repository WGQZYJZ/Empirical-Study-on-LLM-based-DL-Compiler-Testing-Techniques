input_tensor = torch.randn(10, 10)
value = torch.randint(1, 10, (1,))
output_tensor = torch.Tensor.multiply_(input_tensor, value)