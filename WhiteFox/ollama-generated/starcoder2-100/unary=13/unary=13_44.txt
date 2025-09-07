
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(240, 8)
 
    def forward(self, x1):
        v1 = self.linear(x1)
        v2 = torch.sigmoid(v1)
        v3 = v1 * v2
        return v3


# Initializing the model
m = Model()


# Inputs to the model
x1 = torch.randn(4, 80) # Replace with real inputs of 5000 examples each with a shape of [batch_size x number_of_features] such as 240 in our example above.
