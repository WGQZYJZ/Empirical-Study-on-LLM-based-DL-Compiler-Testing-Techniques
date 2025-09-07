
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1):
        v1 = torch.nn.functional.dropout(x1) # Apply dropout to the input tensor
        v2  = torch.rand_like(v1) 
        return v2

m = Model()
x1  = torch.randn(3, 4) # Generating the input tensor for the model

 __output__  = m(x1)
