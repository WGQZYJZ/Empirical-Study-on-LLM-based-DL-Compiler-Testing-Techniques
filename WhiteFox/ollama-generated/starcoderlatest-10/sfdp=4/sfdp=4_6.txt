
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.query_conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
        self.key_conv   = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x):
        qk = self.query_conv(x) @ self.key_conv(x).transpose(-2, -1) / math.sqrt(x.size(-1))
        return torch.softmax(qk + attn_mask, dim=-1)  * value


# Initializing the model
m = Model()
 
# Inputs to the model
q = torch.randn(1, 3, 64, 64)
k = torch.randn(1, 3, 64, 64)
v = torch.randn(1, 8, 64, 64)
 
attn_mask  = torch.zeros(q.size(0), q.size(0), dtype=torch.float32)
