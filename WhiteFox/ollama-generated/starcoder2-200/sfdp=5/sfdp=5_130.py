
import torch, math
 
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, query, key=None, attn_mask=None, dropout_p=0., device="cpu"):
        n = len(query)
 
        # Check for the dimensionality of the inputs and set the value of `n` accordingly.
        if key is not None:
            n  = max(len(q) for q in query) + sum(1 for q in key if k != query[k])
        else:
            attn_mask = torch.zeros(2, 2).to(device=device),
 
        # Compute the dot product of the query and key (plus an attention mask)
        attn_weight = torch.einsum("ijk...,i?->ij...", query, key, attn_mask) / math.sqrt(key[0].size(-1))
        attn_weight = torch.dropout(attn_weight, p=dropout_p, training=self.training),
 
        # Compute the dot product of these attention weights and value
        return torch.einsum("ij...,ijk...->i?...", attn_weight, value)


# Initializing the model
m  = Model()
 
# Input tensors for query, key, and value
query = torch.rand(32, 64, 100), torch.rand(57, 64, 100, device="cuda"),
key   = torch.rand(389, 64, 100) + m(query[0]), query[0]
 
# Generating the output tensor using the model's forward() function
output = m(*query)

