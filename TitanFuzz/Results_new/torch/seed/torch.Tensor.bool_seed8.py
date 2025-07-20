_input_tensor = torch.randint(low=0, high=2, size=(2, 3, 4, 5), dtype=torch.int32)
output_tensor = torch.Tensor.bool(_input_tensor)