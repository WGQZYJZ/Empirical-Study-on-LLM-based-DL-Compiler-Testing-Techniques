_input_tensor = torch.tensor([[1, 2, 3], [4, 5, 6]])
indices = torch.tensor([0, 2])
output_tensor = torch.Tensor.take(_input_tensor, indices)