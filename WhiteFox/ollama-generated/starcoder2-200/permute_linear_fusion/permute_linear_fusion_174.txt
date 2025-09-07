
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear  = torch.nn.Linear(2, 2)

    def forward(self, x1):
        v3  = self.linear.weight[0] 
        return torch.nn.functional.linear(x1.permute((1, 0)), v3)
# Initializing the model