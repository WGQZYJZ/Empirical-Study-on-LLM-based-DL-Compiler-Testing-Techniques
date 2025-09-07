
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.attn_mask = torch.randn((1, 3, 64, 64))
        self.query = torch.randn((2, 8, 64, 64))
        self.key = torch.randn((2, 8, 64, 64))
 
    def forward(self):
        v1 = self.attn_mask @ self.query / math.sqrt(self.query.size(-1))
        v1 = v1 + self.attn_mask
        return v1


# Initializing the model
m = Model()

# Inputs to the model
