input_tensor = torch.randint(0, 10, (3, 4, 5))
output_tensor = torch.Tensor.diag_embed(input_tensor)