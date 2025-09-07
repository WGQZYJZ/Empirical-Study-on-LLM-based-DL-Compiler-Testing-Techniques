
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.attention = torch.nn.MultiheadAttention(8, 4)
 
    def forward(self, query, key, value):
        qk = self.attention(query, key, value)[0] # Apply the multihead attention to compute a scaled dot product of the query and key
        return qk


# Inputs to the model
q1 = torch.randn(4, 3, 64, 64)
k1 = torch.randn(4, 8, 64, 64)
v1 = torch.randn(4, 8, 64, 64)
