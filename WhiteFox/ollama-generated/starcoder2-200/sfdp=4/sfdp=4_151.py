
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.attn = torch.nn.MultiheadAttention(embed_dim=512, num_heads=8)
 
    def forward(self, q, k, v):
        attn_output  = self.attn(q, k, v)[0]
	return attn_output


# Initializing the model and inputs to the model.
m  = Model()
k1 = torch.randn((56,), dtype=torch.float32) # [56]. 2d tensor
v1 = torch.randn((8, 512), dtype=torch.float32).transpose(-2,-1) # [8][512]
q1 = torch.randn(10, 57, 512), k1
__output__  = m(*q1, v1)

