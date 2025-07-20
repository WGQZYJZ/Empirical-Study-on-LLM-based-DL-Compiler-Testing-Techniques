tensor_data_a = torch.tensor([[1, 0, 0], [0, 1, 0], [0, 0, 1]])
tensor_data_b = torch.tensor([[0, 1, 1], [1, 0, 1], [1, 1, 0]])
tensor_data_c = torch.bitwise_or(tensor_data_a, tensor_data_b)