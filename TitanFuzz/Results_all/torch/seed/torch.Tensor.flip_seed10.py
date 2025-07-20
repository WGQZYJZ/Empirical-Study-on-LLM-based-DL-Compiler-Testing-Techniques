input_tensor = torch.randint(0, 10, (2, 3, 4))
output_tensor = torch.Tensor.flip(input_tensor, dims=(0, 1))