
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.qk  = torch.nn.Linear(3, 8)
 
    def forward(self, query1, key1, value1):
        v2 = self.qk(query1)
        v4 = scaled_qk + 1  # Add 1 to the dot product of the query and the key
        return v4


# Initializing the model
m  = Model()

# Inputs to the model
query1 = torch.randn(20, 3)
key1   = torch.randn(5, 8)
value1 = torch.randn(5, 8)
 
# Computation of output using PyTorch
__output__= m(query1, key1, value1)

