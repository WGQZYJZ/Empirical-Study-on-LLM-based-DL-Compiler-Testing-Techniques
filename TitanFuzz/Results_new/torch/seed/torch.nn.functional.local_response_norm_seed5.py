input = Variable(torch.randn(1, 3, 5, 5))
output = torch.nn.functional.local_response_norm(input, size=3, alpha=0.0001, beta=0.75, k=2)