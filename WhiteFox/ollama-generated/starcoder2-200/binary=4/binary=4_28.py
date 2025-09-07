
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(3072, 512)
 
    def forward(self, x):
        v = self.linear(x)
        return v + torch.randn_like(v)


# Initializing the model
m = Model()

# Inputs to the model
input_tensor = torch.randn(3072, 512) # Input tensor of the size [batch size x 3072]

