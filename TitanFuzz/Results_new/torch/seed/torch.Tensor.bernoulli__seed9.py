input_tensor = torch.rand(4, 4)
output_tensor = torch.Tensor.bernoulli_(input_tensor, p=0.5, generator=None)