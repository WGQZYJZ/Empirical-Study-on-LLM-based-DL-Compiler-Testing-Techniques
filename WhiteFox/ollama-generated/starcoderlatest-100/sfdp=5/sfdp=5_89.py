
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.attention = torch.nn.MultiheadAttention(1, 8)
 
    def forward(self, q1, k1, v1):
        output, attn_weight = self.attention(q1, k1, v1)
        return output


# Initializing the model
m = Model()


# Inputs to the model
q1 = torch.randn(1, 8, 64, 64) # Shape [batch size, query length, key length]
k1 = torch.randn(1, 8, 32, 64) # Shape [batch size, query length, value length]
v1 = torch.randn(1, 8, 64, 64) # Shape [batch size, value length, key length]
