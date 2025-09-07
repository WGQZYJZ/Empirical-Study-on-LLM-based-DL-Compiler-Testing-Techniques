
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1):
       v = torch.nn.functional.dropout(x1)  # Apply dropout to the input tensor
       return torch.rand_like(v).sum()


# Initializing the model
m  = Model().to('cpu')

# Inputs to the model
input1  = torch.randn(3, 4, 5)

# Expected output of the model (in float tensor format)
output  = m(input1).sum()
__outputs__ = output

