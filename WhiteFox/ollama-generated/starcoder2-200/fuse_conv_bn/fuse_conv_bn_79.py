m  = torch.nn.Conv1d(4, 20, kernel_size=5)
m2 = torch.nn.Conv1d(30, 20, kernel_size=5)
m  = m2(m(input))

x = torch.randn(2, 4, 60)

__output__  = m(x) # This line will be removed by the fusor
