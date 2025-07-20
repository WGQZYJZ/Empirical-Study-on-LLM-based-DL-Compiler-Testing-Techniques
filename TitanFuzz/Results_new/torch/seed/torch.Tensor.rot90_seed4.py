input_tensor = torch.randn(2, 3, 4)
output_tensor = torch.Tensor.rot90(input_tensor, k=1, dims=(0, 1))