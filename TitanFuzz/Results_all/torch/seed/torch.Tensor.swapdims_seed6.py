input_tensor = torch.randn(2, 3, 5)
output_tensor = torch.Tensor.swapdims(input_tensor, 0, 1)
output_tensor = torch.Tensor.swapdims(input_tensor, 1, 2)
output_tensor = torch.Tensor.swapdims(input_tensor, 2, 0)