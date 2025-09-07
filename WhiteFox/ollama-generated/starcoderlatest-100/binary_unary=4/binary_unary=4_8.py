
class Model(torch.nn.Module):
    def __init__(self, other_tensor=None):
        super().__init__()
        self.linear = torch.nn.Linear(32 * 32 * 1, 8)
        if other_tensor is not None:
            self.other = other_tensor
 
    def forward(self, x1):
        v1 = self.linear(x1.view(-1, 32 * 32)) + (
                if self.other is not None:
                    self.other else torch.zeros((1, 8)))
        v2 = torch.nn.functional.relu(v1)
        return v2


# Initializing the model
m = Model()

x1 = torch.randn(1, 3, 64, 64)
