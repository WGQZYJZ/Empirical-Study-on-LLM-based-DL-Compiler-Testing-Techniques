
class Attention(torch.nn.Module):
    def __init__(self, dim_q, dim_kv, dim_v, dropout_p):
        super().__init__()
        self.conv_q = torch.nn.Conv2d(dim_q, dim_kv, 1, stride=1, padding=0)
        self.conv_k = torch.nn.Conv2d(dim_kv, dim_kv, 1, stride=1, padding=0)
        self.conv_v = torch.nn.Conv2d(dim_kv, dim_v, 1, stride=1, padding=0)
        self.attn_dropout = nn.Dropout(p=dropout_p)
 
    def forward(self, query, key, value):
        qk = self.conv_q(query)  # Shape: [batch size, heads, num of keys, query dim]
        v = self.conv_v(value) # Shape: [batch size, heads, num of values, value dim]
 
        qk = self.attn_dropout(qk) # Dropout on the query
        attn_weight = torch.matmul(qk, key.transpose(-2, -1))  # Shape: [batch size, heads, num of keys, num of values]
        attn_weight = F.softmax(attn_weight, dim=-1)  # Softmax along the last axis
        attn_weight = self.attn_dropout(attn_weight)  # Dropout on the softmax output

        value = torch.matmul(attn_weight, v)  # Shape: [batch size, heads, num of keys, value dim]
        return value


# Initializing the model
attention = Attention(dim_q=128, dim_kv=64, dim_v=32, dropout_p=0.25)


# Inputs to the model
x1 = torch.randn(1, 4, 128, 64) # Shape: [batch size, heads, query dim, key dim]
