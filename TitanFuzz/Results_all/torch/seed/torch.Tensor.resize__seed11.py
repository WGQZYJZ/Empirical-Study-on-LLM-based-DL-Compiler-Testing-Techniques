input_tensor = torch.randint(0, 10, size=(2, 3, 4, 5), dtype=torch.int32)
output_tensor = torch.Tensor.resize_(input_tensor, 2, 3, 4, 5)