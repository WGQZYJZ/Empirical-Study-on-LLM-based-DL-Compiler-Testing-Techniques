
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.fc1 = torch.nn.Linear(3072, 64)
 
    def forward(self, x1):
        t1 = torch.addmm(x1, a_weight, b_weight) + c_bias
        t2 = torch.cat([t1], dim=dim)
        return v6


# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(10, 3072)
