input_tensor = torch.rand(3, 3, 3)
other = torch.rand(3, 3, 3)
output_tensor = torch.Tensor.gcd(input_tensor, other)