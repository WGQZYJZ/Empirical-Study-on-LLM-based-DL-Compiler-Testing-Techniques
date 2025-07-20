input = torch.rand(1, 1, 5, 5)
output = torch.nn.functional.local_response_norm(input, size=2)