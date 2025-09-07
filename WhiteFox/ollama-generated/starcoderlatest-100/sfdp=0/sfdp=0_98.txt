
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.attention = torch.nn.MultiheadAttention(8, 4)
 
    def forward(self, x1, key, query):
        attention_weights = self.attention(x1, key, value=query)
        return output

# Inputs to the model
key = torch.randn(256, 4, 30, 8)
query = torch.randn(128, 4, 9, 17)
