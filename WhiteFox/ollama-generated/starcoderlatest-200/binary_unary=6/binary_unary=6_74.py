
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(64*64, 128)
 
    def forward(self, x1):
        v1 = self.linear(x1.view(-1, 64 * 64))
        v2 = v1 - other
        v3 = torch.nn.functional.relu(v2)
        return v3


# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
