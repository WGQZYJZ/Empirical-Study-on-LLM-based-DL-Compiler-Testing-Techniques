data = [[1, 2], [3, 4]]
tensor_data = torch.tensor(data, dtype=torch.float32, device=torch.device('cpu'), requires_grad=True)
tensor_data = torch.randn(2, 3, dtype=torch.float32, device=torch.device('cpu'), requires_grad=True)
tensor_data