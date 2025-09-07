
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1, x2):
        t3  = torch.cat([x1, x2], dim=0) 
        v4 = self.linear(t3).view(-1, 28, 28)
        v5 = torch.nn.functional.relu(v4)
        return v5

