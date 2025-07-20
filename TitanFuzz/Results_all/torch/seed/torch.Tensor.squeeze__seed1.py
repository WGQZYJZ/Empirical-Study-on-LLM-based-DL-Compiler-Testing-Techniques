input_tensor = torch.rand(2, 1, 2, 1)
output_tensor = torch.Tensor.squeeze_(input_tensor, dim=1)