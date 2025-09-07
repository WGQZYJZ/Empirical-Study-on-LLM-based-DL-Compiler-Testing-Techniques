
class ScaledDotProductAttention(torch.nn.Module):
    def __init__(self, dim_key=128):
        super().__init__()
        self.dim_key = dim_key
 
    def forward(self, query, key, value):
        # Get the number of keys and values in the batch
        batch_size  = query.shape[0]
        n_keys      = torch.tensor([x1.shape[1] for x1 in key])
 
        scaled_dot_product  = torch.matmul(query, key.transpose(-2, -1)) / math.sqrt(self.dim_key)
        attention_weights   = scaled_dot_product.softmax(dim=-1)
        output              = attention_weights.matmul(value)
 
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.attention  = ScaledDotProductAttention()
 
    def forward(self, query, key, value):
        v2          = self.attention(query, key, value)
 
        return v1 * v2
 
# Initializing the model
m = Model()

 # Inputs to the model
x1 = torch.randn(4, 512, 38, 38)
x2 = [torch.randn(4, self.dim_key, 19, 19), torch.randn(4, self.dim_key, 23, 23)]
v2 = m(query=x1, key=x2[0], value=x2[1])

 