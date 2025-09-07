
class MultiHeadSelfAttention(torch.nn.Module):
    def __init__(self, embed_dim: int, num_heads: int):
        super().__init__()
        self.embed_dim = embed_dim
        self.num_heads = num_heads
        # Compute the size of the model's linear layer for computing the query, key, and value in the attention mechanism.
        self._qkv_projection = torch.nn.Linear(embed_dim, embed_dim * 3, bias=False)
        # Create `num_heads` linear layers to compute each head's output of the attention mechanism.
        self._head_projections = [
            torch.nn.Linear(embed_dim, embed_dim, bias=False) for _ in range(self.num_heads)
        ]
 
    def forward(self, x):
        # Apply two linear layers to compute the query, key, and value before entering the attention mechanism.
        b, n, c = x.shape
        qkv = self._qkv_projection(x).view(b, n, 3, -1).transpose(1, 2) # `self._qkv_projection` computes: `(query @ key.transpose(-2, -1)) / math.sqrt(query.size(-1))`
        q, k, v = qkv[0], qkv[1], qkv[2]
        for i in range(self.num_heads):
            # Apply linear layers to compute each head's output of the attention mechanism.
            q_head = self._head_projections[i](q)
            k_head = self._head_projections[i](k)
            v_head = self._head_projections[i](v)
            # Compute the dot product between two tensors for each head and compute softmax. The `i`th element of a tensor is at index `b*n + h*m + i`.
            qkv_attn  = torch.einsum('bnij,bnij->bnhj', q_head, k_head) # `(query @ key.transpose(-2, -1)) / math.sqrt(query.size(-1))`
            attn_weight = softmax(qkv_attn).view(b, n, self.num_heads)
            output = torch.einsum('bnhj,bnij->bnnij', attn_weight, v_head) # `self._head_projections[i]` computes: `(query @ key.transpose(-2, -1)) / math.sqrt(query.size(-1))`
        return output
# Initializing the model
m = MultiHeadSelfAttention(3072, 8)

 # Inputs to the model
x1 = torch.randn(1, 512, 64, 64)
