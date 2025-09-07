
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.multihead_attention = torch.nn.MultiheadAttention(8, 16)
 
    def forward(self, q, k, v):
        attention_weights = self.multihead_attention(q, k, v)[0]
        output = attention_weights.matmul(v)
        return output


# Initializing the model
m = Model()
# Inputs to the model
q = torch.randn(16, 32, 1024, 64)
k = torch.randn(16, 32, 512, 64)
v = torch.randn(16, 32, 1024, 64)
