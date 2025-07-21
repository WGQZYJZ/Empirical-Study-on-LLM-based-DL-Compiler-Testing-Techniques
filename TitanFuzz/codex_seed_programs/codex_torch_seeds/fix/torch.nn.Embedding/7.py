'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.Embedding\ntorch.nn.Embedding(num_embeddings, embedding_dim, padding_idx=None, max_norm=None, norm_type=2.0, scale_grad_by_freq=False, sparse=False, _weight=None, device=None, dtype=None)\n'
import torch
input_data = torch.tensor([[1, 2, 4, 5], [4, 3, 2, 9]])
embedding = torch.nn.Embedding(10, 3)
output = embedding(input_data)
print(output)
"\nTask 4: Call the API torch.nn.EmbeddingBag\ntorch.nn.EmbeddingBag(num_embeddings, embedding_dim, max_norm=None, norm_type=2.0, scale_grad_by_freq=False, mode='mean', sparse=False, _weight=None, per_sample_weights=None, include_last_offset=False, device=None, dtype=None)\n"
embedding_bag = torch.nn.EmbeddingBag(10, 3, mode='sum')
output = embedding_bag(input_data)
print(output)