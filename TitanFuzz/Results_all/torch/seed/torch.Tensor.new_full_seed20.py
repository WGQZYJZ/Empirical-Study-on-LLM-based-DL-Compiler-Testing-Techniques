input_tensor = torch.Tensor([[1, 2, 3], [4, 5, 6]])
output_tensor = torch.Tensor.new_full(input_tensor, size=(2, 3), fill_value=1)