
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.query = torch.nn.Linear(5, 3)
        self.key   = torch.nn.Linear(64, 3)
 
    def forward(self, x1, x2):
        qk = self.query(x1).transpose(-2, -1) @ self.key(x2) / math.sqrt(float(x1.shape[-1]))
        attn_weight = torch.softmax(qk, dim=-1)
        output      = attn_weight @ x2
        return output


# Initializing the model
m  = Model()

