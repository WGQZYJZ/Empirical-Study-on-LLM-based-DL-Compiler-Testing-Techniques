x = torch.tensor([1, 2, 3, 4, 5])
N = 2
torch.vander(x, N)
torch.vander(x, N, increasing=True)