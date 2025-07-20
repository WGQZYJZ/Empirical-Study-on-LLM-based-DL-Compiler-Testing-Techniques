input_tensor = torch.randint(0, 10, (3, 3))
size = (2, 2)
stride = (1, 1)
output_tensor = torch.Tensor.as_strided(input_tensor, size, stride)