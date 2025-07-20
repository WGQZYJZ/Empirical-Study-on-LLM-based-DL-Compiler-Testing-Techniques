input_tensor = torch.rand(2, 3)
output_tensor = torch.Tensor.multinomial(input_tensor, 5, replacement=False)