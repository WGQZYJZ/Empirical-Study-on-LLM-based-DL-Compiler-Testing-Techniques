
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.attn = torch.nn.MultiheadAttention(3, 8)
 
    def forward(self, q, k, v):
        attn_weight = self.attn(q, k, v)[0]
        output = attn_weight @ v
        return output


# Initializing the model
m = Model()


# Inputs to the model
query = torch.randn(1, 3, 64, 64)
key = torch.randn(1, 3, 64, 64)
value = torch.randn(1, 3, 64, 64)
