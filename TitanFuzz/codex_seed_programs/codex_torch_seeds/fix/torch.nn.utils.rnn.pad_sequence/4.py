'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.utils.rnn.pad_sequence\ntorch.nn.utils.rnn.pad_sequence(sequences, batch_first=False, padding_value=0.0)\n'
import torch
input_data = [torch.Tensor([1, 2, 3]), torch.Tensor([4, 5, 6]), torch.Tensor([7, 8, 9]), torch.Tensor([10, 11, 12])]
print(torch.nn.utils.rnn.pad_sequence(input_data, batch_first=True, padding_value=0.0))
print(torch.nn.utils.rnn.pad_sequence(input_data, batch_first=False, padding_value=0.0))
print(torch.nn.utils.rnn.pad_sequence(input_data, batch_first=True, padding_value=0.0).shape)
print(torch.nn.utils.rnn.pad_sequence(input_data, batch_first=False, padding_value=0.0).shape)