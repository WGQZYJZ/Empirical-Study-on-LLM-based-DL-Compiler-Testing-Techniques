input_tensor = torch.rand(2, 3)
output_tensor = torch.Tensor.bernoulli_(input_tensor, p=0.5)