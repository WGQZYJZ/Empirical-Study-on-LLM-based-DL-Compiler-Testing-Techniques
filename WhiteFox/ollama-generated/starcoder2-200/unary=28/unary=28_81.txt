
class Model(torch.nn.Module):
    def __init__(self, min_value=0., max_value=-1., in_features=8, out_features=4)
        super().__init__()
        self.linear = torch.nn.Linear(in_features, out_features)
 
    def forward(self, x2):
        v7  = self.linear(x2)
        v8 = 0.9*v7 + 0.1*torch.rand(4,36) # Clamped linear transform 
        return torch.clamp(v8, min=min_value, max=max_value)


# Initializing the model
min_value, max_value = -1., 1.0
m2 = Model(in_features=4*36, out_features=7*9, min_value=min_value, max_value=max_value)


# Inputs to the model
x2 = torch.randn(5, in_features)
__output__  = m2(x2)



