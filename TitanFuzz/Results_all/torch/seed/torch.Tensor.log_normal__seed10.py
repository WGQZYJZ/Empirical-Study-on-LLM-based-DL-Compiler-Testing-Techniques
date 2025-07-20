input_tensor = torch.rand(2, 3)
output_tensor = torch.Tensor.log_normal_(input_tensor, mean=1, std=2)