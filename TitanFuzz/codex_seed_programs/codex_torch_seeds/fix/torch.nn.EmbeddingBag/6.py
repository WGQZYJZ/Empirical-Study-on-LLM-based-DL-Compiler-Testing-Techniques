"\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.EmbeddingBag\ntorch.nn.EmbeddingBag(num_embeddings, embedding_dim, max_norm=None, norm_type=2.0, scale_grad_by_freq=False, mode='mean', sparse=False, _weight=None, include_last_offset=False, padding_idx=None, device=None, dtype=None)\n"
import torch
import torch
data = [[1, 2, 4, 5], [4, 3, 2, 9]]
embedding = torch.nn.EmbeddingBag(10, 3, mode='mean')
input = torch.tensor(data)
output = embedding(input)
print(output)