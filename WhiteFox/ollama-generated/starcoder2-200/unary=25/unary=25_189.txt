
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear  = torch.nn.Linear(32, 10)
 
    def forward(self, x):
        v1  = self.linear(x)
        return t2 > 0


# Initializing the model and getting inputs for it
m = Model()
input_tensor = torch.randn(5, 32)
 
# Calling the model
output_tensor = m(input_tensor)
