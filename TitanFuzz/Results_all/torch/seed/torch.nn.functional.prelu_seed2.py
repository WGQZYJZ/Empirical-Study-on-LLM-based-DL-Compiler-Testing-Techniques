input_data = torch.tensor([[1, 2, 3], [4, 5, 6]], dtype=torch.float32)
weight = torch.tensor([0.2], dtype=torch.float32)
output = torch.nn.functional.prelu(input_data, weight)