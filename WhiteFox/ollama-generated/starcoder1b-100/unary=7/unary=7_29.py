
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(3, 4)
        self.clamp   = torch.nn.Parameter(torch.tensor([0, -1]), requires_grad=True)
 
    def forward(self, x1):
        v1 = self.linear(x1) + self.clamp  # l2 transform followed by clamp applied to l2 transform
        return torch.relu(v1)


# Initializing the model
m = Model()

