
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(2, 1)
 
    def forward(self, x1, other): 
        v1  = self.linear(x1) + other 
        v3 = F.relu(v1) # Applying ReLU
        return v3

# Initializing the model
m = Model()


# Inputs to the model
__input_tensor__1  = torch.randn(2, 4),
other  = torch.randn(1, 4)


