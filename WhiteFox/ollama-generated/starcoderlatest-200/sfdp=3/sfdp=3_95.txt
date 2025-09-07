
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.attention = torch.nn.MultiheadAttention(embed_dim=32, num_heads=8)
 
    def forward(self, query, key, value):
        qk = self.attention(query, key, value)
        scaled_qk = qk[0].mul(scale_factor)
        softmax_qk = scaled_qk.softmax(dim=-1)
        output = torch.nn.functional.dropout(softmax_qk, p=dropout_p).matmul(value)
        return output

# Inputs to the model
query = torch.randn(8, 20, 32)
key = torch.randn(8, 56, 32)
value = torch.randn(8, 128, 32)
