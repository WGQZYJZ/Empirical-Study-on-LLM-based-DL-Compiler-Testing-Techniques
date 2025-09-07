
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(8, 10)
        other = torch.nn.Parameter(
            torch.zeros([10], dtype=torch.float))
 
    def forward(self, x1):
        v1 = self.linear(x1)
        v2 = v1 - other
        return v2


# Initializing the model
m  = Model()


# Inputs to the model
input_tensor = torch.randn(4096)
__output__  = m(input_tensor)