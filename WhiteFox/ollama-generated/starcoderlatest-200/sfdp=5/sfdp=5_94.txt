
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.query = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
        self.key = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x):
        qk = query @ key.transpose(-2, -1) / math.sqrt(query.size(-1))
        attn_mask = torch.softmax((x > 0).float(), dim=-1) * (x < 0)
        return output


# Initializing the model
m = Model()

# Inputs to the model
query = torch.randn(32, 3, 64, 64)
value = torch.randn(32, 8, 64, 64)
