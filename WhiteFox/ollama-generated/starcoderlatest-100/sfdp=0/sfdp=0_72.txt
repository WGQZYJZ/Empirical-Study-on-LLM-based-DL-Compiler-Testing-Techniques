
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.attention = ScaledDotProductAttention()
 
    def forward(self, query: Tensor, key: Tensor, value: Tensor):
        scaled_dot_product = torch.matmul(query, key.transpose(-2, -1)) / 0.5 ** (0.5 * (torch.tensor(1.0) + key.size(-1)))
        attention_weights = self.attention(scaled_dot_product)
        output = attention_weights.matmul(value)
        return output
# Initializing the model
m = Model()

# Inputs to the model
query  = torch.randn(2, 3, 64, 64)
key = torch.randn(2, 3, 64, 64)
value = torch.randn(2, 8, 64, 64)
