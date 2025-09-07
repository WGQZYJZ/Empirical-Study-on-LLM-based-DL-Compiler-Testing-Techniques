
class Model(torch.nn.Module):
    def __init__(self, other_tensor):
        super().__init__()
        self.linear = torch.nn.Linear(1, 8)
 
    def forward(self, x1):
        v1 = self.linear(x1) + other_tensor
        return v1


# Initializing the model
m = Model()


# Inputs to the model
input_tensor = torch.randn(10)
other  = torch.randn(8)
