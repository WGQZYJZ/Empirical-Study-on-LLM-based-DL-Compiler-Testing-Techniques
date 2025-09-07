
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.attn = torch.nn.Linear(512, 512)
 
    def forward(self, x1):
        qk = self.attn(x1)
        attn_weight = torch.softmax(qk, dim=-1)
        output = self.attn(attn_weight @ x1)
        return output


# Initializing the model
m  = Model()


# Inputs to the model
query = torch.randn(1, 512, 64, 64)
key = torch.randn(1, 512, 64, 64)
