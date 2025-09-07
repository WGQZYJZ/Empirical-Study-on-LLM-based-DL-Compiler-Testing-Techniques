
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.attention = ScaledDotProductAttention()
 
    def forward(self, query, key, value):
        scaled_dot_product  = torch.matmul(query, key.transpose(-2, -1)) / inv_scale
        attention_weights = scaled_dot_product.softmax(dim=-1)
        output = attention_weights.matmul(value)
        return output
 
 # Initializing the model
m = Model()

 # Inputs to the model
 query  = torch.randn(2, 8, 5, 5)
 key  = torch.randn(2, 3, 4, 4)
 value = torch.randn(2, 4, 5, 6)
