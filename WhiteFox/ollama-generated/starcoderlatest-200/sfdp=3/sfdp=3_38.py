
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.attention = torch.nn.MultiheadAttention(8, 8)
 
    def forward(self, q1, k1, v1):
        attention_output, _ = self.attention(q1, k1, v1)
        return attention_output
# Initializing the model
m = Model()

# Inputs to the model
query  = torch.randn(2, 8, 64, 64)
key    = torch.randn(2, 8, 64, 64)
value  = torch.randn(2, 8, 64, 64)
