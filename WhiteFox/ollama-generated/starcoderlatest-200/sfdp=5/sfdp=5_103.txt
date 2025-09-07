
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.query = torch.nn.Linear(32, 32)
        self.key = torch.nn.Linear(32, 32)
 
    def forward(self, qk, value, key_mask, attn_mask):
        v1 = self.query @ self.key.transpose(-2, -1) / math.sqrt(self.key.size(-1))
        v1 = torch.tanh(v1 + kq + m) * 0.5 + qk + value
        return v1


# Initializing the model
m = Model()

 # Inputs to the model
qk = torch.randn(2, 32, 32)
value = torch.randn(2, 8, 64, 64)
key_mask = (torch.rand(*qk.size()) < dropout_p).detach()
attn_mask = (torch.rand(*qk.size()) < dropout_p).detach()
