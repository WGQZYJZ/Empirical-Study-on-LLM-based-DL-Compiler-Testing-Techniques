
class MultiHeadAttention(torch.nn.Module):
    def __init__(self, query_dim: int, key_dim: int,
                 value_dim: int, num_heads: int, dropout_p: float):
        super().__init__()
 
        self.query_layer = torch.nn.Linear(query_dim, query_dim)
        self.key_layer = torch.nn.Linear(key_dim, key_dim)
        self.value_layer = torch.nn.Linear(value_dim, value_dim)
        
        # 3D Tensor with shape [B, N, (N // num_heads), heads, d_k]
        self.q_proj_layer = torch.nn.Linear(query_dim, num_heads * d_k)
        self.k_proj_layer = torch.nn.Linear(key_dim, num_heads * d_k)
        self.v_proj_layer = torch.nn.Linear(value_dim, num_heads * d_v)
        
        # 3D Tensor with shape [B, N, (N // num_heads), heads, d_v]
        self.o_proj_layer = torch.nn.Linear(num_heads * d_v, query_dim)
        
    def forward(self, query: Tensor, key: Tensor, value: Tensor):
        q_t = self.query_layer(query)  # [B, N, heads, d_k]
        k_t = self.key_layer(key)  # [B, N, heads, d_k]
        v_t = self.value_layer(value)  # [B, N, heads, d_v]
        
        # Project the three tensors to 3D Tensors with shape [B, N, (N // num_heads), heads, d_k], [B, N, (N // num_heads), heads, d_k], and [B, N, (N // num_heads), heads, d_v]
        q_t = self.q_proj_layer(q_t)  # [B, N, (N // num_heads), heads, d_k]
        k_t = self.k_proj_layer(k_t)  # [B, N, (N // num_heads), heads, d_k]
        v_t = self.v_proj_layer(v_t)  # [B, N, (N // num_heads), heads, d_v]
 
        scaled_qk = torch.matmul(q_t, k_t.transpose(-2, -1))  # [B, N, (N // num_heads), heads, d_k]
        softmax_qk = scaled_qk.softmax(dim=-1)  # [B, N, (N // num_heads), heads, d_k]
        
        dropout_qk = torch.nn.functional.dropout(softmax_qk, p=dropout_p)  # [B, N, (N // num_heads), heads, d_k]
        output = torch.matmul(dropout_qk, v_t)  # [B, N, (N // num_heads), heads, d_v]

        o_t = self.o_proj_layer(output)  # [B, N, heads, d_v]

        # Shape: [B, N, heads, d_k]
        q_t = torch.cat([q_t, k_t], dim=-1).permute(0, 2, 1, 3, 4)  # [B, heads, N, (N // num_heads), d_k + d_k]
 
        return o_t * dropout_prob, q_t


# Initializing the model
attention = MultiHeadAttention(query_dim=d_model, key_dim=d_model,
                             value_dim=d_model, num_heads=num_heads,
                             dropout_p=dropout_p)
 
# Inputs to the model
q1 = torch.randn(8, 32, d_model)
k1 = torch.randn(8, 32, d_model)
v1 = torch.randn(8, 32, d_model)
__output__, __context__ = attention(q1, k1, v1)

