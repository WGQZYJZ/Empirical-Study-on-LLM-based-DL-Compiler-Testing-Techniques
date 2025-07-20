input_tensor = torch.empty(100, 100)
output_tensor = torch.Tensor.bernoulli_(input_tensor, p=0.5, generator=None)