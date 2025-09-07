
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1, other):
        v1 = self.linear1(x1)
        v2 = v1 - other
        v3 = torch.relu(v2) # relu is torch.nn.functional.relu()
        return v3

# Initializing the model and passing an additional input tensor as a parameter in forward function of the model.
m  = Model()
x1, oth = torch.randn((100, 4)), 2 * (torch.ones(10)) # x1 is an input to the model. oth - 2*one, is additional input tensor we need to pass in the forward() function of our model.
