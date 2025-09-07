
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.query = torch.nn.Linear(512, 2048)
        self.key   = torch.nn.Linear(512, 2048)
        self.value = torch.nn.Linear(512, 2048)
 
    def forward(self, x):
        qk = F.linear(x, self.query, self.key).transpose(-2, -1) / math.sqrt(x.size(-1))
        attn_weight = F.softmax(qk, dim=-1)
        output = torch.matmul(attn_weight, self.value)
        return output

# Initializing the model
m = Model()


# Inputs to the model
q = torch.randn(20, 512, 7, 7)
k = torch.randn(20, 512, 7, 7)
v = torch.randn(20, 512, 6, 6)
