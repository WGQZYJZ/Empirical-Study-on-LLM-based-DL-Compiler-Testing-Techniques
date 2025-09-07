
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.query = torch.nn.Linear(3, 12) 
        self.key = torch.nn.Linear(3, 8) 
        self.value = torch.nn.Linear(4, 6)
 
    def forward(self, qk_mask):
        qk = self.query @ self.key.transpose(-2, -1) / math.sqrt(self.query.size(-1)) 
        qk = qk + qk_mask
        attn_weight = torch.softmax(qk, dim=-1) 
        output = attn_weight @ self.value 
        return output


# Initializing the model
m = Model()

# Inputs to the model
qk_mask  = torch.randn(16, 3, 64, 64)
__output__  = m(qk_mask)

