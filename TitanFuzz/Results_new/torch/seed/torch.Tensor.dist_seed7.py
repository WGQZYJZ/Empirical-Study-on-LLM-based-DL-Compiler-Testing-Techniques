input_tensor = torch.randn(1, 3)
output_tensor = torch.Tensor.dist(input_tensor, input_tensor, p=2)