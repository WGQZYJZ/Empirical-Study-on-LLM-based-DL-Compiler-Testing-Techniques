input = torch.randn(1, 1, 5, 5)
output = torch.nn.functional.local_response_norm(input, size=2, alpha=0.0001, beta=0.75, k=1.0)