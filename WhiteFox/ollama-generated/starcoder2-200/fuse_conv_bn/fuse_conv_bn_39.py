
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1): 
        return torch.nn.functional.batch_norm(
            torch.nn.functional.conv1d(x1), 
            weight=None, bias=None, running_mean=0., running_var=0.)


# Initializing the model 
m = Model()

# Inputs to the model 
input = torch.randn(4, 2)


__output__  = m(input)

