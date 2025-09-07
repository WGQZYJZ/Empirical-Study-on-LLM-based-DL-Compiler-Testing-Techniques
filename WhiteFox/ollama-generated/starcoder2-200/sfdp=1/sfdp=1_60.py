
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.attn  = torch.nn.MultiheadAttention()
 
    def forward(self, query, key, value):
       v1  = self.attn(query=query, key=key)
       return v1


# Initializing the model
m = Model()
 
# Inputs to the model
q = torch.randn(32, 64, 768) # Query tensor with 768 features and a batch size of 32.
k = torch.randn(32, 64, 768) # Key tensor with 768 features and a batch size of 32.
v = torch.randn(32, 192, 512) # Value tensor with 512 features and a batch size of 32.
 
# Run the model with inputs q, k, v
__output__  = m(q, k, v)
