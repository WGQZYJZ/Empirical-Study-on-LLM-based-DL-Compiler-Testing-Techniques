'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.utils.rnn.pack_padded_sequence\ntorch.nn.utils.rnn.pack_padded_sequence(input, lengths, batch_first=False, enforce_sorted=True)\n'
import torch
import torch.nn as nn
import torch
import torch.nn as nn
input = torch.randn(3, 5, 4)
lengths = [5, 3, 1]
padded_input = nn.utils.rnn.pack_padded_sequence(input, lengths, batch_first=True)
print(padded_input)
'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.utils.rnn.pad_packed_sequence\ntorch.nn.utils.rnn.pad_packed_sequence(sequence, batch_first=False, padding_value=0.0, total_length=None, return_lengths=False)\n'
import torch
import torch.nn as nn
import torch
import torch.nn as nn