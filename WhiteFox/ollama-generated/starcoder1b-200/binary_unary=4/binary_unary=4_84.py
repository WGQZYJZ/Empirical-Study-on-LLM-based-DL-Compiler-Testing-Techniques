
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(32, 16)
 
    def forward(self, x1, other=None):
        v1 = self.linear(x1) + (other or 0.)
        v2 = torch.relu(v1)
        return v2


# Inputs to the model
input_tensor  = torch.randn(4, 32, 16)
