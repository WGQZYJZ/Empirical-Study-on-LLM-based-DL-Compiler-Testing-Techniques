input_tensor = torch.rand(10)
output_tensor = torch.Tensor.exponential_(input_tensor, lambd=1, generator=None)