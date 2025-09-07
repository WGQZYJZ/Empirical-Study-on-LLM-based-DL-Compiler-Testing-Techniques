
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(256 * 8 * 49 + 2, int(70 / (1 - 0.3)), bias=True)
 
    def forward(self, x1, x2):
        v1 = torch.cat([x1, x2], dim=-1)
        v1 = v1.view(-1, self.linear.in_features)
        v2 = self.linear(v1)
        return v2


# Initializing the model