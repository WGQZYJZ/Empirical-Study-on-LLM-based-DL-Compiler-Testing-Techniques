
class Attention(nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, query, key, value):
       scaled_dot = torch.matmul(query,  key) / math.sqrt(key.size(-1))
       attention_weights = scaled_dot.softmax(dim=-1)
       output =  attention_weights.matmul(value) 
       return output
 

# Initializing the model
m = Attention()

 # Inputs to the model
query = torch.randn(32, 64)
key = torch.randn(32, 500)
value = torch.randn(32, 800)
__output__  = m(query, key, value)
