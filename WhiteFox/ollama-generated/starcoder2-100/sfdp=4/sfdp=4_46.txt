
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1):
        v2  = self.__output__
        v3  = torch.transpose(v2, -2, -1) / math.sqrt(v2.size(-1))
        v4  = v3 + attn_mask
        attn_weight  = torch.softmax(v4, dim=-1)
        v7  = x1 @ attn_weight
        return v7


# Initializing the model
m = Model()

# Inputs to the model
x2 = torch.randn(36805, 9375)
attn_mask  = torch.ones(36805, 9375).cuda()
__output__  = m(x1)

