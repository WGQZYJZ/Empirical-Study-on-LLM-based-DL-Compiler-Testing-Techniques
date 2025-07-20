input_data = torch.randn(2, 5)
target_data = torch.tensor([3, 4])
loss = torch.nn.functional.cross_entropy(input_data, target_data)