
class AttentionLayer(torch.nn.Module):
    def __init__(self, dim1, dim2):
        super().__init__()
        self.attn = torch.nn.MultiheadAttention(dim_in=dim1, num_heads=8)
        self.dropout = torch.nn.Dropout()
        self.linear = torch.nn.Linear(dim2, 64)
 
    def forward(self, qk):
        attn_weight = self.attn(qk)[0]
        output = self.dropout(attn_weight) @ qk
        return self.linear(output)


# Initializing the model
a1 = AttentionLayer(256, 1024)
