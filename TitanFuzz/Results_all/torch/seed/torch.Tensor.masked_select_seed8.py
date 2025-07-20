input_tensor = torch.tensor([[1.0, 2.0, 3.0], [4.0, 5.0, 6.0], [7.0, 8.0, 9.0]])
mask = torch.tensor([[0, 0, 1], [1, 0, 0], [0, 0, 1]])
output_tensor = torch.Tensor.masked_select(input_tensor, mask)