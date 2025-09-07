
class ScaledDotProductAttention(torch.nn.Module):
    def __init__(self, attention_dim, scale=None):
        super().__init__()
        self.scale = scale or math.sqrt(attention_dim)

    def forward(self, qk, v):
        # qk: (N, Lq, dim), shape of `scaled_dot_product` input tensor, which is used to compute attention weights
        # v:  (N, d_model, length_v)
        N, Lq, d = qk.shape
        _, d_model, length_v = v.shape

        # Compute scaled dot product
        qk = torch.matmul(qk, kq) / self.scale
        attention_weights = qk.softmax(dim=-1)
        
        # Compute context vector and output tensor with shape (N, Lq, dim)
        v = v * attention_weights
        return v 
class ScaledDotProductAttentionWithPadding(ScaledDotProductAttention):
    def __init__(self, q_dim, k_dim, dim, scale=None):
        super().__init__(attention_dim=(q_dim if dim > q_dim else dim) * (k_dim if dim > k_dim else dim), scale=scale)

    def forward(self, query, key):
        return super().forward(query.transpose(-2, -1).contiguous(), key.transpose(-2, -1).contiguous())


# Inputs to the model
qk = torch.randn(1, 8, 64, 64)  # (batch_size, length_q, num_features), where qk is defined as a query vector and v is defined as the value vector
v  = torch.randn(1, 8, 256, 192)  # (batch_size, length_v, hidden_dim)
