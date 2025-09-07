
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.lin = torch.nn.Linear(32, 8)
 
    def forward(self, x1):
        v1  = self.lin(x1)
        v2  = v1 + other # Add another tensor (specified by the keyword argument "other") to the output of the linear transformation
        return v2


# Initializing the model with two input tensors (the size of each is [N, 32]).
m = Model(x1=torch.randn(30, 32), other=torch.randn(30, 8))

 # Inputs to the model
x1 = torch.randn(5, 32)
 
 # The output of the model (in the shape [N, 8]) is v2 in the model.
