input_tensor = torch.Tensor([[1, 2, 3], [4, 5, 6]])
indices = torch.LongTensor([0, 2])
output_tensor = torch.Tensor.take(input_tensor, indices)