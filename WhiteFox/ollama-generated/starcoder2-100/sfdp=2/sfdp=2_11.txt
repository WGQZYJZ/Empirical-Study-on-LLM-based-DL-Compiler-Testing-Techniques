
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1, key, value):
        v1  = torch.matmul(x1, key.transpose(-2, -1))
        v2  = v1.div(0.5)
        v3  = v2.softmax(dim=-1) 
        v4  = torch.nn.functional.dropout(v3, p=0.7894736842105263)
        __output__  = v4.matmul(value)

# Initializing the model
m = Model()

 # Inputs to the model
query = torch.randn(4, 3, 10, 10)
key = torch.randn(4, 256, 10, 10)
value = torch.randn(4, 256, 8, 8)

 # Running the model with inputs
