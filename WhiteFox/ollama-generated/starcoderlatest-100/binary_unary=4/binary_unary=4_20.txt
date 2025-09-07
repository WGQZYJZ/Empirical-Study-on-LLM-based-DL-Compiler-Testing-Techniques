
class Model(torch.nn.Module):
    def __init__(self, other=None):
        super().__init__()
        self.linear = torch.nn.Linear(3, 8)
        if other is None:
            other = torch.randn(10)
        else:
            other = torch.rand(10)
        self.other_tensor = other
 
    def forward(self, x1):
        v1 = self.linear(x1)
        v2 = v1 + self.other_tensor
        v3 = torch.nn.functional.relu(v2)
        return v3


# Initializing the model with some initial parameter values (such as a learned embedding vector for each token, a learned matrix to convert a document word index to an encoded representation of its meaning)
m = Model()
initial_parameters = {}
