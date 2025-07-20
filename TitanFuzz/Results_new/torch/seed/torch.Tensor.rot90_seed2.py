input_tensor = torch.rand(2, 3, 4)
rotate_tensor = torch.Tensor.rot90(input_tensor, 2, [0, 1])