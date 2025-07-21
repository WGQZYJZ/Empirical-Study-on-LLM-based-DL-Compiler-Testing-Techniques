'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.utils.rnn.pad_sequence\ntorch.nn.utils.rnn.pad_sequence(sequences, batch_first=False, padding_value=0.0)\n'
import torch
sequences = [torch.Tensor([1, 2, 3]), torch.Tensor([4, 5, 6, 7]), torch.Tensor([8, 9])]
batch_first = False
padding_value = 0.0
print(torch.nn.utils.rnn.pad_sequence(sequences, batch_first, padding_value))