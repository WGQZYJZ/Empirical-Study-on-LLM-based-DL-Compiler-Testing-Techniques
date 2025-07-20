input_tensor = torch.arange(start=0, end=9, step=1).reshape(3, 3)
output_tensor = torch.Tensor.flip(input_tensor, dims=[0])