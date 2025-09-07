
class MultiHeadAttention(torch.nn.Module):
    def __init__(self, head_dim, num_heads=8):
        super().__init__()

        self.head_dim = head_dim
        self.num_heads = num_heads
        self.scale = (self.head_dim ** -0.5)

    def forward(self, q, k, v, mask=None):
        # QKV is a tensor of shape (batch_size * n_seq, heads, seq_len, dim), where the last two dimensions are the query, key and value tensor respectively
        bsz, n_q, _, _ = q.shape
        bsz, n_k, _, _ = k.shape
        bsz, n_v, _, _ = v.shape

        assert n_q == n_k == n_v, 'Q, K, V should have the same number of batches and sequence lengths'

        # (batch_size * n_seq) x heads
        scaled_dot_product  = torch.matmul(q, k.transpose(-2,-1)) / self.scale

        if mask is not None:
            assert mask.shape == (bsz, n_q, n_k), 'The dimensions of attention mask and query/key tensor do not match'
            scaled_dot_product = torch.where(scaled_dot_product > 0,
                                            scaled_dot_product,
                                            1e-5 * torch.ones_like(scaled_dot_product))

        # (batch_size * n_seq) x heads
        attention_weights = torch.softmax(scaled_dot_product, dim=-1)

        # Batch size x sequence length x heads x dimension
        context = torch.matmul(attention_weights, v)

        return context, attention_weights
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.attn = MultiHeadAttention(8)
 
    def forward(self, q, k, v, mask=None):
        # QKV is a tensor of shape (batch_size * n_seq, heads, seq_len, dim), where the last two dimensions are the query, key and value tensor respectively
        context, _ = self.attn(q, k, v, mask)

        return context
# Initializing the model
m = Model()

# Inputs to the model
q = torch.randn(1, 3, 64, 64)
k = torch.randn(1, 8, 64, 64)
v = torch.randn(1, 8, 64, 64)
mask = torch.zeros_like(q[:,:,:5,:]) > 0
