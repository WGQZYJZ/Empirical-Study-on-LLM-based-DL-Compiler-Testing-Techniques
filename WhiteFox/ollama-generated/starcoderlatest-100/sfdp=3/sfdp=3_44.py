
class TransformerAttention(torch.nn.Module):
    def __init__(self, key_dim, num_heads):
        super().__init__()
        self.num_heads = num_heads
        self.attention = torch.nn.Linear(key_dim, num_heads)
 
    def forward(self, query, key, value, scale_factor, dropout_p):
        