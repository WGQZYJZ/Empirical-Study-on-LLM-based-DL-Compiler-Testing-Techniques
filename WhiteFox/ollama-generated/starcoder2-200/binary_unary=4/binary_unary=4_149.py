
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear  = torch.nn.Linear(28 * 28, 10)
 
    def forward(self, x1): 
        v1  = self.linear(x1.view(-1))
        v3 = v1 + other 
        return relu(v3)


# Initializing the model with the keyword argument `other` passed as a parameter to its forward method
m  = Model()
other  = torch.randn([28, 28])


# Inputs to the model
x1  = torch.randn(500, 784)

 # Run the model and verify that it matches the previous results
