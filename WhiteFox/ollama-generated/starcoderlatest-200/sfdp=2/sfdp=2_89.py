
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(768, 3072)
 
    def forward(self, x1):
        v1 = x1 @ self.linear.weight + self.linear.bias 
        return v1


# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(1, 768)
