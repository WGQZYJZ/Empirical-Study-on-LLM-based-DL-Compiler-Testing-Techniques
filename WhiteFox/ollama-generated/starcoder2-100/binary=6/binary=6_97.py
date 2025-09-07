
class Model2(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(3, 4)
 
    def forward(self, x1):
        v1 = self.linear(x1) 
        v2 = v1 - other # subtract 'other' from the output of linear transformation.
        return v2

# Initializing the model
m2 = Model()


# Inputs to the model
x1  = torch.randn(3, 3)# This model takes an input with a size [batch_size X 3]. It has a single output
other = 0.5 # this is another tensor or scalar that we want to subtract from the output of linear transformation.
__output__  = m2(x1)

