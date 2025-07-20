input_tensor = torch.randn(2, 3, 4, 5, 6)
output_tensor = torch.Tensor.swapdims(input_tensor, 0, 1)