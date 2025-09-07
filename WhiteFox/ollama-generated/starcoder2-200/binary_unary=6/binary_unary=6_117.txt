
class Model2(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear1 = torch.nn.Linear(64, 32)
 
    def forward(self, x1):
        v1 = self.linear1(x1) 
        v2 = v1 - other
        return relu(v2)


# Initializing the model
m2 = Model()


# Inputs to the model
x1  = torch.randn(1, 64)
other = np.random.rand() * 5 + .001 # Adding a small constant (otherwise it will be 0) for better precision in testing

# Initializing a new constant that is not present in the previous model
other2 = other + 1

 __output__  = m(x1, other, other2)
 
 