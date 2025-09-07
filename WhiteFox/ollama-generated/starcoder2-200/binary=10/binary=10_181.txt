
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(64, 32)
 
    def forward(self, x1, other):
        v1 = self.linear(x1)
        v2 = v1 + other # Add another tensor to the output of the linear transformation
        return v2


# Initializing the model and passing two tensors (tensors that do not need to be provided by the user). 
m = Model()
other  = torch.randn(3, 8)
__output__1 = m(x1, other) # The output tensor of the model is different from previous one

