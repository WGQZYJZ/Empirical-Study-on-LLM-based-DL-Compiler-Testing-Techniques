
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear  = torch.nn.Linear(3, 8)
 
    def forward(self, x1):
        v2 = self.linear(x1, other) 
        v4 = relu(v5)
        return v6


# Initializing the model<|end_of_code|>
m  = Model()


# Inputs to the model
x1 = torch.randn(3, 8)
other = torch.randn(3, 8)

