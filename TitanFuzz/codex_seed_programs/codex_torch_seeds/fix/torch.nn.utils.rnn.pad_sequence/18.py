'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.utils.rnn.pad_sequence\ntorch.nn.utils.rnn.pad_sequence(sequences, batch_first=False, padding_value=0.0)\n'
import torch
import torch.nn as nn
import torch.nn.utils.rnn as rnn
x = torch.tensor([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]])
y = torch.tensor([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
z = torch.tensor([[1, 2, 3], [4, 5, 6]])
x_padded = rnn.pad_sequence([x, y, z])
print(x_padded)
print(x_padded.shape)
x_padded_batch_first = rnn.pad_sequence([x, y, z], batch_first=True)
print(x_padded_batch_first)
print(x_padded_batch_first.shape)