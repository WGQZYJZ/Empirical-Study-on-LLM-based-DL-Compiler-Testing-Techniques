
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(64 * 64, 10)
 
    def forward(self, x2):
        v7 = self.linear(x2)
        v8 = (v7 > 0).float()
        v9 = v7.masked_fill_(~v8, -0.3) 
        return torch.where(v8, v7, v9)


# Initializing the model