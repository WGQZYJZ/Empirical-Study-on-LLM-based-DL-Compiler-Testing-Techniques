'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.LSTM\ntorch.nn.LSTM(input_size, hidden_size, num_layers=1, bias=True, batch_first=False, dropout=0.0, bidirectional=False, proj_size=0, device=None, dtype=None)\n'
import torch
import torch
X = torch.randn(1, 1, 3)
lstm = torch.nn.LSTM(3, 3)
(out, _) = lstm(X)
print(out)
print(out.shape)