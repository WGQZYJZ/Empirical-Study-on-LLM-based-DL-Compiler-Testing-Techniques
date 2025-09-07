
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.attn = torch.nn.MultiheadAttention()
 
    def forward(self, query, key, value):
        attn_output  = self.attn(query, key, value)
        return attn_output[0]

# Initializing the model
m  = Model()

 # Inputs to the model
query  = torch.randn(128, 32, 64)
key  = torch.randn(128, 64, 37)
value  = torch.randn(128, 64, 50)
