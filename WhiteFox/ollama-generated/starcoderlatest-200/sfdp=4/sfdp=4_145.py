
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.attn = torch.nn.MultiheadAttention(
            query_dim=64, key_dim=128, num_heads=4)
 
    def forward(self, q, k, v):
        _, attn_weight  = self.attn(q, k, v)
        output            = attn_weight @ v
        return output


# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(2, 64, 1024)
x2 = torch.randn(3, 512, 768)
