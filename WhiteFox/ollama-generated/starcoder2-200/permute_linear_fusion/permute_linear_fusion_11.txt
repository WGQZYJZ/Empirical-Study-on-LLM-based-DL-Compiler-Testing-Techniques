
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear  = torch.nn.Linear(2, 1)

    def forward(self, x1): 
        v1  = x1.permute(0, 2, 1).sum(dim=1)
        return torch.nn.functional.softmax(v1 + torch.tensor([5]), dim=-1), self.linear(x1)

# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(2, 3)

