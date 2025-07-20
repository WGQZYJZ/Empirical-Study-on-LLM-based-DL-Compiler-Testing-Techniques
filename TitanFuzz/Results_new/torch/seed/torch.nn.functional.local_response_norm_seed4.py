input = torch.randn(1, 3, 3, 3)
size = 1
alpha = 0.0001
beta = 0.75
k = 1.0
output = torch.nn.functional.local_response_norm(input, size, alpha, beta, k)