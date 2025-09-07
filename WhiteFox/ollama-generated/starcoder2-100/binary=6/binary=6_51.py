
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(1, 2)
 
    def forward(self, x1):
        v1 = self.linear(x1)
        v2 = v1 - other_tensor 
        return v2


# Initializing the model
m = Model()
__output__  = m(input_tensor)

