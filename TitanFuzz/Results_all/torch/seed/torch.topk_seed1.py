x = torch.tensor([[1, 2, 3], [4, 5, 6]])
k = 1
dim = 1
largest = True
sorted = True
y = torch.topk(x, k, dim, largest, sorted)