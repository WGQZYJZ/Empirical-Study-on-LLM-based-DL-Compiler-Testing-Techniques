_input_tensor = torch.randn(2, 3)
_output_tensor = torch.Tensor.bernoulli_(_input_tensor, p=0.5, generator=None)