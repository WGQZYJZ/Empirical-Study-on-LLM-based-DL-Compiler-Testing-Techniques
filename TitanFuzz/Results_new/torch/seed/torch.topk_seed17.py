input = torch.randn(10, 5, 10)
k = 2
dim = 2
largest = True
sorted = True
topk_result = torch.topk(input, k, dim, largest, sorted)