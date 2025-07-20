a = torch.rand(3, 4)
b = torch.rand(3, 4)
c = torch.column_stack((a, b))
c = torch.column_stack((a, b), out=torch.FloatTensor(3, 8))