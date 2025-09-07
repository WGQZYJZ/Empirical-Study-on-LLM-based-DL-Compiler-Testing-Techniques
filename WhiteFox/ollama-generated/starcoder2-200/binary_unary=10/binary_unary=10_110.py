
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear  = torch.nn.Linear(307201, 45)
        self.linear2 = torch.nn.Linear(45, 90)
 
    def forward(self, x1):
        v1 = self.linear(x1) + other # Here we have added the `other` tensor to the result of the linear transformation
        v3 = self.linear2(v1)
        return v3


# Initializing the model
m  = Model()
 
