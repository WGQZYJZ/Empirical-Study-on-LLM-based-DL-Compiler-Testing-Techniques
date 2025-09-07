
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.query = torch.nn.Linear(4, 16)
        self.key   = torch.nn.Linear(4, 16)
        self.value = torch.nn.Linear(16, 1)
 
    def forward(self, x1):
        qk = self.query(x1).matmul(self.key.transpose(-2, -1)) / math.sqrt(x1.size(-1))
        attn_weight = torch.softmax(qk, dim=-1)
        v    = self.value(attn_weight @ x1)
        return v


# Initializing the model
m = Model()


