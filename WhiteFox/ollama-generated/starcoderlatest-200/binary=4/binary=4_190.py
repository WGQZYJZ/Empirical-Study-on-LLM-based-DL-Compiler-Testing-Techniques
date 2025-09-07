
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(8096, 256)
 
    def forward(self, x1):
        v1 = self.linear(x1)
        v2 = v1 + other_tensor
        return v2


# Initializing the model
m = Model()

 # Inputs to the model
x1 = torch.randn(8096, 3, 14, 14)

 # Other tensor to add (specified by the keyword argument "other_tensor")
other_tensor = torch.randn(256, 3, 14, 14)
 
