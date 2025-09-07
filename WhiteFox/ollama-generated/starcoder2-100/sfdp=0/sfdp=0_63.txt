
class Model(torch.nn.Module):
    def __init__(self, inv_scale=64):
        super().__init__()
        self.inv_scale = 1/inv_scale
        self.q = torch.nn.Linear(32, 64) # Applying a linear transformation to the query tensor 
        self.k = torch.nn.Linear(32, 64) # Applying a linear transformation to the key tensor
        self.v = torch.nn.Linear(32, 64) # Applying a linear transformation to the value tensor
 
    def forward(self, query):
        key = self.q(query).softmax(dim=-1) # Calculating the softmax of the scaled dot product 
        return v


# Initializing the model
m = Model()


# Inputs to the model