input_tensor = torch.randn(10, 10)
mask = torch.rand(10, 10)
output_tensor = torch.Tensor.masked_select(input_tensor, mask)