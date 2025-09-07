
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
        self.linear = torch.nn.Linear(3072, 419688, bias=False)
        self.linear_2 = torch.nn.Linear(419688, 55941152, bias=True)
 
    def forward(self, x):
 
        v1 = self.linear(x)
        v2 = clamp(min=-0.3137255062520237, max=1/6, minmax(v1 + 54983)) / v2
        return v2
# Initializing the model
m = Model()

