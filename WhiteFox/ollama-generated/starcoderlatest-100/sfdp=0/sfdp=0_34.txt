
class MultiHeadAttention(torch.nn.Module):
    def __init__(self, d_model: int = 768, num_heads: int = 12):
        super().__init__()
        self.d_k = d_model // num_heads 
        self.num_heads = num_heads 

        self.w_qs = torch.nn.Linear(d_model, num_heads * d_k)
        self.w_ks = torch.nn.Linear(d_model, num_heads * d_k)
        self.w_vs = torch.nn.Linear(d_model, num_heads * d_v)
        
        self.attention = torch.nn.Softmax(-1)  # Attention scores are unscaled!

    def transpose_for_scores(self, x: torch.Tensor): 
        new_x_shape = x.size()[:-1] + (self.num_heads, ) + (self.d_k, )
        x = x.view(*new_x_shape)
        
        return x.permute(0, 2, 1, 3)  # Transpose to shape [batch_size, head_num, seq_len, hidden_dim]

    def forward(self, q, k, v):
        batch_size = q.shape[0]
        q = self.w_qs(q).view(batch_size, -1, self.num_heads, self.d_k)  # (bsz, len, num_heads, head_dim)

        k = self.w_ks(k).view(batch_size, -1, self.num_heads, self.d_k)
        v = self.w_vs(v).view(batch_size, -1, self.num_heads, self.d_v)

        q = self.transpose_for_scores(q)  # (bsz, num_heads, len, head_dim)

        if k is not None:
            k = self.transpose_for_scores(k)  # (bsz, num_heads, len, head_dim)

        if v is not None:
            v = self.transpose_for_scores(v)  # (bsz, num_heads, len, head_dim)
    
        attention_weights = self.attention(q @ k.transpose(-2, -1))  # (bsz, num_heads, len, len)

        if v is not None:
            output = attention_weights * v

        else:
            output = attention_weights
        
        output = torch.transpose(output, 1, 2).contiguous()
        output = output.view(-1, batch_size, self.num_heads * self.d_v)  # (bsz * num_heads, seq_len, hidden_dim)

        return output


class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
        self.attention = MultiHeadAttention(768, 4)
 
    def forward(self, x1):
        v1 = self.conv(x1)
        attention_output = self.attention(v1, None, None)
        return attention_output


# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(2048, 3, 64, 64)
