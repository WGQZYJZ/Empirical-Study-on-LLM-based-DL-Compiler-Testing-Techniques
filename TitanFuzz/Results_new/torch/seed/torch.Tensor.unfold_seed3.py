input_tensor = torch.rand(1, 3, 7, 7)
output_tensor = torch.Tensor.unfold(input_tensor, dimension=2, size=3, step=1)