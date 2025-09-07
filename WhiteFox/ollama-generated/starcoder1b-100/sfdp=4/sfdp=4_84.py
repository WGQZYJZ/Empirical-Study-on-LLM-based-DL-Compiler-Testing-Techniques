
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.query = torch.nn.Linear(3, 4)
        self.key   = torch.nn.Linear(3, 5)
        self.value = torch.nn.Linear(4, 5)
        self.mask  = torch.nn.Parameter(torch.zeros((2, 4, 5)), requires_grad=False)
 
    def forward(self, x1):
        query = self.query(x1)
        key   = self.key(x1)
        value = self.value(x1)
        attn_mask = torch.sparse.softmax(self.mask, -1).type(torch.float32)
        qk  = query @ key.transpose(-2, -1) / math.sqrt(query.size(-1))
        attn_weight = torch.softmax(qk, dim=-1)
        output = attn_weight @ value
        return output


# Initializing the model
m  = Model()

# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
