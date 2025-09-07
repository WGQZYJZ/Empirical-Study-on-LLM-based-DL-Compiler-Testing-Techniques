
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self,  x1):
 
        qk = torch.einsum("abcij, jik -> abcjk", x1)
        qk = qk + torch.ones([32], device=x1.device).view(-1, 1 , 64, 64)
        attn_weight = torch.softmax(qk, dim=-1)
 
        return attn_weight

m  = Model()

# Initializing the model
x1 = torch.randn(32, 8, 512)
__output__  = m(x1)

