

class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear1 = torch.nn.Linear(32, 50)
 
    def forward(self, x1):
        v1  = self.linear1(x1)
        v2  = v1 + other_tensor_from_outside_the_model
        return v2


# Initializing the model
m  = Model()


# Inputs to the model
x1  = torch.randn(5, 32)

other_tensor_from_outside_the_model  = torch.ones(5, 50)
__output__  = m(x1)