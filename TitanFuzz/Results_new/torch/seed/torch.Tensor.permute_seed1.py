input_tensor = torch.rand(2, 3, 4)
output_tensor = torch.Tensor.permute(input_tensor, 1, 2, 0)