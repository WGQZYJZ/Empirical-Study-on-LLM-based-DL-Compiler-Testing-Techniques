input_tensor = torch.randn(3, 4, 5)
output_tensor = torch.Tensor.swapdims(input_tensor, 0, 2)