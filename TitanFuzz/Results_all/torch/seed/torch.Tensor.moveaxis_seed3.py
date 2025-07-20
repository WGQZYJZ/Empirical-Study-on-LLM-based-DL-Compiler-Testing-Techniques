input_tensor = torch.randint(low=0, high=10, size=(2, 3, 4), dtype=torch.int)
output_tensor = torch.Tensor.moveaxis(input_tensor, 0, (- 1))