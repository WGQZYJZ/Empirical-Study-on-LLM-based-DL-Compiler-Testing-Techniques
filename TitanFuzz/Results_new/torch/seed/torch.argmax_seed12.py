input_data = torch.tensor([[0.1, 0.2, 0.3], [0.3, 0.2, 0.1], [0.4, 0.5, 0.6], [0.6, 0.5, 0.4]])
result = torch.argmax(input_data, dim=1)
input_data = torch.tensor([[0.1, 0.2, 0.3], [0.3, 0.2, 0.1], [0.4, 0.5, 0.6], [0.6, 0.5, 0.4]])
result = torch.argmax(input_data, dim=1, keepdim=True)