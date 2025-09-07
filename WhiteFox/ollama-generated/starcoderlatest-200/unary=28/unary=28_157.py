
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(64*64*3, 128)
 
    def forward(self, x1):
        v1 = self.linear(x1)
        v2 = torch.clamp_min(v1, min_value)
        v3 = torch.clamp_max(v2, max_value)
        return v3


# Initializing the model
m = Model()
min_value  = torch.randn((), requires_grad=True)
max_value  = torch.randn((), requires_grad=True)

# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
