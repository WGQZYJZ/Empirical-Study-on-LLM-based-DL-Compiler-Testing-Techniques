
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(512, 8)
 
    def forward(self, x):
        v0 = self.linear(x)
        v1 = v0 + other
        return v1


# Initializing the model and setting "other" to an arbitrary value. 
m = Model()
v_other = torch.randn(512).view(-1, 8)
