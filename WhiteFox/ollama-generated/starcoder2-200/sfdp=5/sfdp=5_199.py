
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.attn = torch.nn.MultiheadAttention(64, 128)
 
    def forward(self, query, key, value):
        v10  = self.attn(query, key, value)[0] # Apply multi-headed attention on the inputs `query`, `key` and `value`.
        return v10


# Initializing model
m = Model()
 
# Input to the model
input_query   = torch.randn(32, 64)
input_key     = torch.randn(32, 64)
input_value   = torch.randn(32, 192) # The number of keys should be equal to the number of values
 
__output__  = m(input_query, input_key, input_value)

