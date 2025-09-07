
class MultiHeadAttention(torch.nn.Module):
    def __init__(self, h_dim=None):
        super().__init__()
        self.head_num = 4  # The number of heads for multi-head attention layer
        if h_dim is not None:
            self.h_dim = h_dim
 
        self.q_proj = torch.nn.Linear(query.shape[-1], query.shape[-1])
        self.k_proj = torch.nn.Linear(key.shape[-1], key.shape[-1])
        self.v_proj = torch.nn.Linear(value.shape[-1], value.shape[-1])
 
        self.out_proj = torch.nn.Linear(dropout_qk.shape[-1], dropout_qk.shape[-1])
 
    def forward(self, x1):
        v1  = self.q_proj(query).unsqueeze(-2)
        v2  = self.k_proj(key).unsqueeze(-3)
        v3  = self.v_proj(value).unsqueeze(-3)
 
        scaled_qk  = torch.matmul(v1, v2.transpose(-2, -1)) / math.sqrt(self.h_dim)
        softmax_qk  = scaled_qk.softmax(dim=-1)
        dropout_qk  = torch.nn.functional.dropout(softmax_qk, p=dropout_p)
 
        output = self.out_proj(dropout_qk).squeeze(-3).matmul(v3).transpose(-2, -1)
        return output


class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.multihead_attention = MultiHeadAttention()
 
    def forward(self, x1):
        attention  = self.multihead_attention(x1)
        