
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1, x2):
        v7  = torch.einsum("ijl,ilm->imj", (x2.transpose(-2,-1), x2))
        v8  = self._inner_product(v7)
 
        return v8, v4
 
    @staticmethod
    def _inner_product(qk):
        v9  = qk @ qk.transpose(-2, -1) / math.sqrt(qk.size(-1)) + v2
        attn_weight = torch.softmax(v9, dim=-1).type(torch.float32)
 
        return attn_weight
 
    def backward(self): ...
 
# Initializing the model