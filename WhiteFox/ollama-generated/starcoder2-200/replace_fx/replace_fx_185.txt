
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1):
        v1  = torch.nn.functional.dropout(x1, p=0.5)
        v2  = torch.rand_like(v1) 
        return v2

m = Model()

 # Inputs to the model 
 x1 = torch.randn(3, 4)

 # Call the model with an input tensor 
 