
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1):
         t2  = torch.nn.functional.dropout(x1, p=0) # Dropout input tensor
         t3  = torch.rand_like(t2)
         return t3
# Initializing the model
m = Model()
# Inputs to the model
x1 = torch.randn(1, 5)
