'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.RNNBase\ntorch.nn.RNNBase(mode, input_size, hidden_size, num_layers=1, bias=True, batch_first=False, dropout=0.0, bidirectional=False, proj_size=0, device=None, dtype=None)\n'
import torch
import torch.nn as nn
input_size = 3
hidden_size = 3
num_layers = 3
rnn = nn.RNNBase(mode='RNN_RELU', input_size=input_size, hidden_size=hidden_size, num_layers=num_layers)
print(rnn)
print('Parameters: ', list(rnn.parameters()))
print('Parameter size: ', list(rnn.parameters()))
print('Parameter size: ', [p.numel() for p in rnn.parameters()])
print('Parameter size: ', sum([p.numel() for p in rnn.parameters()]))
print('Parameter size: ', sum([p.numel() for p in rnn.parameters() if p.requires_grad]))