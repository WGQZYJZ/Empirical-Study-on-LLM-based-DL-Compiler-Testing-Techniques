
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear  = torch.nn.Linear(20,3)
 
    def forward(self, x1):
        v1 = self.linear(x1) 
        v2 = v1 + other_tensor  # A different tensor from the previous model.
        v3 = F.relu(v2) # A different activation function than the ReLU in Model.
        return v3


# Initializing the model
m = Model()


# Inputs to the model
x1  = torch.randn(64, 20)
other_tensor = torch.randn(128, 72) # A new tensor from the previous model example
