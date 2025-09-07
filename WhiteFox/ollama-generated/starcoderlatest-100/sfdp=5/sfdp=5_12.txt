
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.attn = torch.nn.MultiheadAttention(num_heads=4, num_key_channels=32, num_value_channels=32)
 
    def forward(self, query, key, value, attn_mask=None):
        qk = self.attn(query, key, value, attn_mask)  # The input of MultiheadAttention is the output of the previous layer
        return qk
