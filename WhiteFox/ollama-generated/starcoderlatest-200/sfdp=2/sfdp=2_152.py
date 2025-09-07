
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.attn = torch.nn.MultiheadAttention()
 
    def forward(self, qk_query, value):
        v2  = self.attn(qk_query, query, key)[0]
        output = v2 * 0.5
        return output

 # Initializing the model
m = Model()

# Inputs to the model
qk_query = torch.randn(1, 8, 64, 64)
value = torch.randn(1, 32, 64, 64)
