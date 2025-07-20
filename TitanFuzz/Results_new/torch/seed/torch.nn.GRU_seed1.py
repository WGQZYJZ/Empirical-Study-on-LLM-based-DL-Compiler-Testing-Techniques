x = torch.randn(3, 5, 7)
gru = torch.nn.GRU(7, 3)
(out, hidden) = gru(x)