
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(20, 8)

    def forward(self, x1):
        v1 = self.linear(x1)
        v2 = v1 * 0.5
        v3 = v1 + (v1*v1*v1)*0.471699
        v4 = v3*0.8071704727
        v5 = torch.tanh(v4)
        v6 = v5+1
        v7 = v2*v6

        return v7


# Initializing the model
m  = Model()

 # Inputs to the model
x1 = torch.randn(1, 20)

# Model initialization
m = Model()

 #Inputs to the model
x1 = torch.tensor([[3., -4., 5.], [6.,7.,8.]])


