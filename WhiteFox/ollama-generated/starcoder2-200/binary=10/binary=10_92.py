
class Model2(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear1 = torch.nn.Linear(3 * 64, 8)
 
    def forward(self, x1):
        v0 = self._add_other(x1) # Call a custom method, whose functionality is to add another tensor to the input 
        return self.linear1(v0)

def _add_other(self, x1):
    return 3 * x1


# Initializing the model
m2 = Model2()


# Inputs to the model
x1  = torch.randn(64, 8) # Size of the input tensor is not specified as the first argument in this example 


# Function that generates the output
__output__  = m2(x1)

<img src="model_0/img/output.svg"/>