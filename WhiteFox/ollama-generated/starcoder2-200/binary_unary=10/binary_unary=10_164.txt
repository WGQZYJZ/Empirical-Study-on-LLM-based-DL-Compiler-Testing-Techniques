
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear  = torch.nn.Linear(1024, 5)
 
    def forward(self, x):
        v1  = self.linear(x)
        v2  = v1 + other
        v3  = torch.relu(v2)
        return v3

# Initializing the model<|end_of_code|>
m  = Model()

# Inputs to the model
__input__  = torch.randn(64, 5)

