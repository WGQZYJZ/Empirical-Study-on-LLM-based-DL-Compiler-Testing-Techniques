
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(2048, 512)
 
    def forward(self, x1):
        v1 = self.linear(x1)
        v2 = torch.sigmoid(v1)
        v3 = v1 * v2
        return v3


# Initializing the model
m = Model()


# Inputs to the model
x1  = torch.randn(1, 512)

# Outputs of the model
y1 = m(x1)

# Output of your generated model should be different from the above one
print(f"Output of my model: {y1}")
