
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(3,10)

    def forward(self, x2, other):
        v1  = self.linear(x2) 
        return v1 + other


# Initializing the model
m = Model()
 
# Inputs to the model (first input should be a tensor and second argument will be an integer number).
x3= torch.randn(5, 3)   # input tensor for  first  argument of the forward function
v2 = x3 + 5              # another tensor in the forward method of the module
