input = torch.empty(2, 3, dtype=torch.float32)
input[(0, 0)] = 0.1
input[(0, 1)] = 0.2
input[(0, 2)] = 0.3
input[(1, 0)] = 1.1
input[(1, 1)] = 1.2
input[(1, 2)] = 1.3
result = torch.isreal(input)