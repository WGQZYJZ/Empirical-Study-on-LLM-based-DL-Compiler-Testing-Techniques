'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.functional.embedding\ntorch.nn.functional.embedding(input, weight, padding_idx=None, max_norm=None, norm_type=2.0, scale_grad_by_freq=False, sparse=False)\n'
import torch
import torch.nn as nn
import torch
import torch.nn as nn
word_to_ix = {'hello': 0, 'world': 1}
embeds = nn.Embedding(2, 5)
lookup_tensor = torch.tensor([word_to_ix['hello']], dtype=torch.long)
hello_embed = embeds(lookup_tensor)
print(hello_embed)
lookup_tensor_2 = torch.tensor([word_to_ix['world']], dtype=torch.long)
world_embed = embeds(lookup_tensor_2)
print(world_embed)