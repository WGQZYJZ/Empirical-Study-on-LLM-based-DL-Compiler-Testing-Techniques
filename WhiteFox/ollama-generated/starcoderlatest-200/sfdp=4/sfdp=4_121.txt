
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.query = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
        self.key = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
        self.value = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1, x2):
        qk  = self.query(x1) @ self.key(x2).transpose(-2, -1) / math.sqrt(self.query.size(-1)) 
        qk = qk + torch.nn.Parameter(torch.randn_like(qk), requires_grad=True)
        attn_weight  = torch.softmax(qk, dim=-1) 
        output = attn_weight @ self.value(x2)
        return output
# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(2, 3, 64, 64)
x2 = torch.randn(2, 3, 64, 64)
