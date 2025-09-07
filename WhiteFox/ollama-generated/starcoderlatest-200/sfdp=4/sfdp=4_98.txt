
class Attention(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.query = torch.nn.Linear(512, 256)
        self.key = torch.nn.Linear(512, 256)
 
    def forward(self, query, key, value):
        qk = (query @ self.key.transpose(-2, -1) / math.sqrt(query.size(-1))).softmax(dim=-1) + attention_mask
        output = (qk @ self.value).transpose(-2, -1)
        return output
 
class MultiHeadAttention(torch.nn.Module):
    def __init__(self, h):
        super().__init__()
        self.attentions = torch.nn.ModuleList()
 
        for _ in range(h):
            self.attentions.append(Attention())
 
    def forward(self, query, key, value):
        attn_output = []
 
        for att in self.attentions:
            x1 = att(query, key, value)  # Shape of the output from each layer is (batch, head, seq_len, dim)
            attn_output.append(x1)
 
        return torch.cat(attn_output, dim=1)
 

# Initializing the model
m2 = MultiHeadAttention(h=8)


# Inputs to the model
q1 = torch.randn(1, 16, 512)  # Shape of `q` is (batch, head, seq_len, dim)
k1 = torch.randn(1, 16, 512)  # Shape of `k` is (batch, head, seq_len, dim)
v1 = torch.randn(1, 16, 512)  # Shape of `v` is (batch, head, seq_len, dim)


# 