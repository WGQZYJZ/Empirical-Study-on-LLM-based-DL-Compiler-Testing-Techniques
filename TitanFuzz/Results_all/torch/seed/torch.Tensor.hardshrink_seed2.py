input_tensor = torch.randn(2, 3, dtype=torch.float32)
output_tensor = torch.Tensor.hardshrink(input_tensor, lambd=0.5)