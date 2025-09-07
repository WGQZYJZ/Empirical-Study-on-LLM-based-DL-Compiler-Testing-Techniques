
class ScaledDotProductAttention(torch.nn.Module):
    def __init__(self, scale=None):
        super().__init__()
        self.scale = scale
 
    def forward(self, query, key, value):
        dot_product = torch.matmul(query, key.transpose(-2, -1)) / (
            (self.scale or 1) ** 0.5 if key is not None else None
        )
        return dot_product
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.attention = ScaledDotProductAttention()
 
    def forward(self, q, k, v):
        attention_weights  = self.attention(q, k, v)
        return torch.matmul(v, attention_weights.permute(0, 2, 1).unsqueeze(-1)).squeeze(-1)
# Initializing the model
m = Model()

