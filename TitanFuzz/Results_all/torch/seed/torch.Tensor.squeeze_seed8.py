input_tensor = torch.rand(1, 3, 3, 3)
output_tensor = torch.Tensor.squeeze(input_tensor, dim=0)