'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.utils.rnn.pack_padded_sequence\ntorch.nn.utils.rnn.pack_padded_sequence(input, lengths, batch_first=False, enforce_sorted=True)\n'
import torch
from torch.autograd import Variable
import torch
from torch.autograd import Variable
batch_size = 2
max_length = 5
hidden_size = 8
input = Variable(torch.randn(batch_size, max_length, hidden_size))
lengths = [5, 3]
packed_input = torch.nn.utils.rnn.pack_padded_sequence(input, lengths, batch_first=True)
print(packed_input)
(padded_output, output_lengths) = torch.nn.utils.rnn.pad_packed_sequence(packed_input, batch_first=True)
print(padded_output)
print(output_lengths)