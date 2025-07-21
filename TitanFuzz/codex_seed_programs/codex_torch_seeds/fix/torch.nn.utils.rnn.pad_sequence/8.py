'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.utils.rnn.pad_sequence\ntorch.nn.utils.rnn.pad_sequence(sequences, batch_first=False, padding_value=0.0)\n'
import torch
data = [torch.rand(3, 3), torch.rand(4, 3), torch.rand(2, 3)]
padded = torch.nn.utils.rnn.pad_sequence(data)
print(padded)