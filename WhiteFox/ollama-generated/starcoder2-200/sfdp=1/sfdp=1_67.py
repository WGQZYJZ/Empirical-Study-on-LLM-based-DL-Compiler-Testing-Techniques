
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.attn = torch.nn.MultiheadAttention(d_model=768, num_heads=12)

    def forward(self, q1):
        v1  = q1
        v2  = torch.randn(30, 48)
        v3  = torch.zeros([15, 9]) 
        v4, _  = self.attn(q1, k=v2, v=v3)
        return v4


# Initializing the model
m  = Model()
# Inputs to the model
q1  = torch.randn(10, 768).long()
__output__  = m(q1)

