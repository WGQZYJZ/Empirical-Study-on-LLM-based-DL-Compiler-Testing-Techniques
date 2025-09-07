
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(64 * 2 * 3, 10)
 
    def forward(self, x1):
        v1 = self.linear(x1)
        return torch.clamp_min(v1, min_value=torch.tensor([1e-4], device='cpu'))


# Initializing the model
m = Model()

