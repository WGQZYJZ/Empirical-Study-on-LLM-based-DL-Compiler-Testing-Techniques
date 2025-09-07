
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1, x2):
        v3 = torch.matmul(x1, x2) / 4
        v6 = v3 + v3
        return v6


# Initializing the model
m  = Model()

 # Inputs to the model
x1  = torch.randn(8, 5) # Query matrix (shape [batch_size, number of query vectors])
x2  = torch.randn(4, 8) # Key/value matrix (shape [number of key/value pairs per vector, batch size])

 