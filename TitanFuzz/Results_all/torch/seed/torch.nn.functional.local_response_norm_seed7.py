dtype = torch.FloatTensor
input = Variable(torch.randn(1, 5, 5).type(dtype), requires_grad=True)
output = torch.nn.functional.local_response_norm(input, size=3, alpha=0.0001, beta=0.75, k=1.0)