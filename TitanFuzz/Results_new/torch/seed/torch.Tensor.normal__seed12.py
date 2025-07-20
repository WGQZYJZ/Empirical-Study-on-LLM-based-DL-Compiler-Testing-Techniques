input_tensor = torch.randn(10, 3)
output_tensor = torch.Tensor.normal_(input_tensor, mean=0, std=1)