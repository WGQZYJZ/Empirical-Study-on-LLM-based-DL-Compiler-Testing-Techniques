
class Model(torch.nn.Module):
    def __init__(self, n_input):
        super().__init__()
        self.linear = torch.nn.Linear(n_input, 10)
 
    def forward(self, x1):
        v1 = self.linear(x1)
        v2 = v1 + self.other # Added this line
        return v2
 

# Initializing the model with one input tensor
m = Model(3)


# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)

# Adding another tensor as an additional input
self.other = torch.randn(2, 20)

