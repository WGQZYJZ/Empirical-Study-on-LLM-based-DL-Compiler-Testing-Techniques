input_size = 3
hidden_size = 4
input = torch.randn(4, 3, requires_grad=True)
hx = torch.randn(4, 4, requires_grad=True)
gru_cell = torch.nn.GRUCell(input_size, hidden_size)