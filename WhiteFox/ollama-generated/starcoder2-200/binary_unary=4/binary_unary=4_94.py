
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear  = torch.nn.Linear(28*28, 10)
 
    def forward(self, x):
        v1  = self.linear(x.view(-1, 28 * 28)) 
        return relu(v1 + other)


# Initializing the model
m = Model()


# Inputs to the model
other = torch.randn(50, 4713) # Other is a randomly initialized tensor of size (50 x 4713)
__input_to_the_model__  = torch.rand(50, 28*28)


__output__  = m(__input_to_the_model__)
