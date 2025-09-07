
class Model(torch.nn.Module):
    def __init__(self, input_dim=32, output_dim=64, hidden_dim=8):
        super().__init__()
        self.linear1 = torch.nn.Linear(input_dim, hidden_dim)
        self.linear2 = torch.nn.Linear(hidden_dim, output_dim)
 
    def forward(self, x1):
        v1  = self.linear1(x1)
        v2  = self.linear2(v1)
        return v2


# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(8, input_dim=32)
