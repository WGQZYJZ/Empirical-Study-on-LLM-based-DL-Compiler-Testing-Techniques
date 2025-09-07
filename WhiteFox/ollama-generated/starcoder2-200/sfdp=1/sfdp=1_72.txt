
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.query  = torch.nn.Linear(10, 5) 
        self.key  = torch.nn.Linear(20, 10)
        self.value  = torch.nn.Linear(30, 20)
 
    def forward(self, query):
        k1  = self.query(query) # Apply linear transformation to the input tensor (linearly transforming its values)
        k2  = self.key(k1) # Apply another linear transformation to the output of the previous transformation 
        v3  = self.value(k2) # Apply another linear transformation to the output of the previous transformation
        out = torch.matmul(v3, query.transpose(-2, -1))  # Compute the dot product between a value tensor and a query tensor using a matrix multiplication
        return out

# Initializing the model
m  = Model()


# Inputs to the model
x1  = torch.randn(5, 5)


__output__  = m(x1)

