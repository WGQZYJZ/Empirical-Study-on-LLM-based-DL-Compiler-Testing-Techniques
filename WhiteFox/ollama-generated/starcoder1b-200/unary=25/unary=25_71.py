
class Model(torch.nn.Module):
    def __init__(self, input_dimension, hidden_dimension=32):
        super().__init__()
        self.linear = torch.nn.Linear(input_dimension, hidden_dimension)
 
    def forward(self, x1):
        v1  = self.linear(x1)
        v2 = torch.where(v1 > 0, v1, negative_slope * v1)
        return v2


# Initializing the model
m = Model(64)


