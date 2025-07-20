data = torch.rand(5, 3)
torch._assert((data.size(0) == 5), 'The first dimension of data should be 5')