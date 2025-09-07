
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(4, 32)
 
    def forward(self, x1):
        v0 = self.linear(x1)
        v1 = v0 + 3
        v2 = F.clamp_min_(v1, min=0)
        v3 = F.clamp_max_(v2, max=6)
        v4 = torch.div(v3, 6.)
        return v4


# Initializing the model
m  = Model()


# Inputs to the model
x1  = torch.randn(10, 4)
__output__  = m(x1)

# The model you generate should be different from the previous one.
# It is important that the input tensor and the output of your new model is the same as in the previous example, otherwise you will not be able to pass the test!
