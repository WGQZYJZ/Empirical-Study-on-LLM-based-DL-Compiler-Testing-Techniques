
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(128, 3)
 
    def forward(self, x):
        v0 = self.linear(x)
        v1 = v0 + 3
        v2 = torch.clamp_min(v1, 0)
        v3 = torch.clamp_max(v2, 6)
        v4 = v3 / 6
        return v4


# Initializing the model and printing model architecture
m = Model()
print(m)

# Inputs to the model with batch size of 128
x = torch.randn(10, 128).double()

# Outputs from the model on the inputs
y = m(x)