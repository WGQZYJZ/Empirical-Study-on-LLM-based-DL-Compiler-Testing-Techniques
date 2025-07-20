input_data = torch.Tensor([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
output_data = torch.Tensor.bernoulli_(input_data, p=0.5)