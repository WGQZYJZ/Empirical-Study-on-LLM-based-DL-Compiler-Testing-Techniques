
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1):
        v1 = self.linear(x1) # Linear transformation on an input tensor
        v2 = v1 + other  # Add another tensor to the output of linear transformation

        return v2


# Initializing the model
m = Model()
other = torch.randn_like(x1)
__output__  = m(x1, other=other)