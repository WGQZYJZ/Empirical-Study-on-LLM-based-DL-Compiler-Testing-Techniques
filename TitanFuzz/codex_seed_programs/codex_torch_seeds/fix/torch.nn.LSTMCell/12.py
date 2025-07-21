'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.LSTMCell\ntorch.nn.LSTMCell(input_size, hidden_size, bias=True, device=None, dtype=None)\n'
import torch
import torch
input_seq = torch.randn(10, 3, 4)
hx = torch.randn(3, 4)
cx = torch.randn(3, 4)
lstm_cell = torch.nn.LSTMCell(4, 4)
for i in range(input_seq.size(0)):
    (hx, cx) = lstm_cell(input_seq[i], (hx, cx))
    print('hx: ', hx)
    print('cx: ', cx)
    print(('-' * 20))