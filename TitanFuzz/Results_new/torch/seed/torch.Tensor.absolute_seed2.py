_input_tensor = torch.randint(low=(- 10), high=10, size=(2, 2))
_absolute_output = torch.Tensor.absolute(_input_tensor)