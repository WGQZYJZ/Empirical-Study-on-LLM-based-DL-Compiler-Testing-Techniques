input_tensor = torch.rand(10, 10)
output_tensor = torch.Tensor.bernoulli_(input_tensor, p=0.5)