
class Model(torch.nn.Module):
    def __init__(self, input_dim=256, hidden_dim=30):
        super().__init__()
        self.linear1 = torch.nn.Linear(input_dim, hidden_dim)
        self.relu  = torch.nn.ReLU()

    def forward(self, t0):
       return self.relu(self.linear1(t0))

# Initializing the model
m = Model()

 # Inputs to the model
input  = torch.randn((1, 256))
__output__  = m(input)

