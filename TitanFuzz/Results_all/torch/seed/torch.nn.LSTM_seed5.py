X = torch.randn(1, 1, 3)
lstm = torch.nn.LSTM(3, 3)
(out, _) = lstm(X)