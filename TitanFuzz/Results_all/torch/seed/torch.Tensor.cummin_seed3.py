_input_tensor = torch.tensor([[1, 2, 3, 4, 5], [1, 2, 3, 4, 5]])
cummin_result = torch.Tensor.cummin(_input_tensor, dim=1)