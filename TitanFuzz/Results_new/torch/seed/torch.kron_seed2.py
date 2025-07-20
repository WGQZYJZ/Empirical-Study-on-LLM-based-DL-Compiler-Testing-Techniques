input = torch.tensor([[1, 2, 3], [4, 5, 6]])
other = torch.tensor([[1, 2], [3, 4], [5, 6]])
torch.kron(input, other)
torch.kron(input, other, out=torch.FloatTensor())