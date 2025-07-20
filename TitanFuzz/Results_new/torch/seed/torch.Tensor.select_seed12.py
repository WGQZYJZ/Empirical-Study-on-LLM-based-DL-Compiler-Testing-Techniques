input_tensor = torch.rand(5, 3)
output_tensor = torch.Tensor.select(input_tensor, dim=1, index=2)