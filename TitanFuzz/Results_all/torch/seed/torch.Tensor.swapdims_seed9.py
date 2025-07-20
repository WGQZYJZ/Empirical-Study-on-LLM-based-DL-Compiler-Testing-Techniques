input_tensor = torch.tensor([[[1, 2, 3], [4, 5, 6], [7, 8, 9]]])
output_tensor = torch.Tensor.swapdims(input_tensor, 0, 1)