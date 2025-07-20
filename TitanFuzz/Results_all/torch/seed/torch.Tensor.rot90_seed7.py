input_tensor = torch.arange(0, 24)
input_tensor = input_tensor.view(2, 3, 4)
output_tensor = torch.Tensor.rot90(input_tensor, 1, [1, 2])