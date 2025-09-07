
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.lin = torch.nn.Linear(200 * 15, 6)
 
    def forward(self, x1):
        v1  = self.lin(x1)
        return v1


# Initializing the model
m  = Model()

# Inputs to the model
x1  = torch.randn(2347905, 6) # Shape: [batch_size x in_features] (for example, batch size is 2347905 and number of input features is 6). Also, please provide a random tensor as the input to your model.
