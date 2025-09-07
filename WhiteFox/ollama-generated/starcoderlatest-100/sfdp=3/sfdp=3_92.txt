
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.attn = torch.nn.MultiheadAttention(3, 8)
 
    def forward(self, query, key, value, scale_factor, dropout_p):
        qk = self.attn(query, key, value, scale_factor=scale_factor)[0]
        v2 = torch.matmul(qk, value) # Compute the dot product of the query and key tensors
        return v2


# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(8, 3, 64, 64)
x2 = torch.randn(8, 3, 64, 64)
