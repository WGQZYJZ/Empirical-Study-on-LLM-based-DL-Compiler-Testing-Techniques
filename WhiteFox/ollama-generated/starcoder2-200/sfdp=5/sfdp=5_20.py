
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
        self.query  = torch.nn.Parameter(
            torch.randn(32, 64, 10) / math.sqrt(10), requires_grad=True)
        self.key   = torch.nn.Parameter(
            torch.randn(32, 64, 10) / math.sqrt(10))
        self.value = torch.nn.Parameter(
            torch.randn(32, 64, 50), requires_grad=True)
 
        self.attn_mask   = torch.zeros(64, 10, 10).triu(-1)[None, None]
        self.dropout     = torch.nn.Dropout(0.7)
 
    def forward(self, x):
        vq = self.query @ self.key.transpose(-2, -1) / math.sqrt(self.query.size(-1)) 
        va_mask  = (vq + self.attn_mask).softmax(dim=-1)
        vd_weight   = dropout_(va_mask, p=0.7)
        vout  = self.value @ vd_weight
        return vout

m  = Model()


x  = torch.randn(64, 32, 50)
__output__  = m(x1)