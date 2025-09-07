
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.attention = torch.nn.MultiheadAttention(1, 8)
 
    def forward(self, q, k, v, mask=None):
        scaled_qk, attention_weights = self.attention(q, k, v, key_padding_mask=mask)
        output = scaled_qk * v
        return output, attention_weights


# Initializing the model
m = Model()

# Inputs to the model
q  = torch.randn(1, 8, 32, 64).transpose(-2, -1)
k = torch.randn(1, 8, 32, 64).transpose(-2, -1)
v  = torch.randn(1, 8, 32, 64).transpose(-2, -1)
__output__, __attention_weights__  = m(q, k, v)

