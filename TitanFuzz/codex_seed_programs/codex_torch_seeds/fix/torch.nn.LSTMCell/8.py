'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.LSTMCell\ntorch.nn.LSTMCell(input_size, hidden_size, bias=True, device=None, dtype=None)\n'
import torch
input = torch.randn(3, 10)
hx = torch.randn(3, 20)
cx = torch.randn(3, 20)
lstm_cell = torch.nn.LSTMCell(10, 20)
(hx, cx) = lstm_cell(input, (hx, cx))
print(hx.shape)
print(cx.shape)