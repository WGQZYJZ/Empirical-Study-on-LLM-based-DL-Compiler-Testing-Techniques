
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.query = torch.nn.Linear(768, 768)
        self.key = torch.nn.Linear(768, 768)
        self.value = torch.nn.Linear(768, 768)
 
    def forward(self, query, key, value):
        qk = query @ key.transpose(-2, -1) / math.sqrt(query.size(-1)) # Compute the dot product of the query and key, and scale it
        qk = qk + attn_mask # Add the attention mask to the scaled dot product
        attn_weight = torch.softmax(qk, dim=-1) # Apply softmax to the result
        output = attn_weight @ value # Compute the dot product of the attention weights and the value
        return output


# Input tensor
x1 = torch.randn(128, 768)  # batch size x sequence length x hidden dim
y1 = torch.randn(32, 768)   # batch size x head num x sequence length x head dim
z1 = torch.randn(4096, 768) # batch size x seq_len x heads x embed_dim


