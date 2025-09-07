
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.attn = torch.nn.MultiheadAttention(num_heads=2, key_dim=32)
 
    def forward(self, x1, x2):
        qk  = self.attn(x1, x2)[0]
        attn_weight = torch.softmax(qk, dim=-1) # Apply softmax to the result
        output = attn_weight @ x2
        return output


# Initializing the model
m = Model()


# Inputs to the model
x1  = torch.randn(2, 32, 64, 64)
x2  = torch.randn(2, 8, 64, 64)
