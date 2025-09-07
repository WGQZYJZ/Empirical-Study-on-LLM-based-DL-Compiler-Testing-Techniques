
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.attention = torch.nn.MultiheadAttention(8, 4)
 
    def forward(self, query, key, value):
        v1, attn_weight = self.attention(query, key, key, need_weights=True)
        output = v1 + value
        return output


# Initializing the model
m = Model()
# Inputs to the model
x = torch.randn(2, 4, 64, 64)
x2 = torch.randn(3, 8, 64, 64)
