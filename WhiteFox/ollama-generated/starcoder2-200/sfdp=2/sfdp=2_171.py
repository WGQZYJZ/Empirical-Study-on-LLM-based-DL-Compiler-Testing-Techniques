
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.dot  = torch.nn.Linear(64, 32)

    def forward(self, query, key, value):
        v1  = torch.nn.functional.dropout(key.transpose(-2, -1), p=0.5, inplace=False) # Apply dropout to the softmax output
        v2  = self.dot(query) 
        v3  = v2 * v1 
        return v3

# Initializing the model
m  = Model()

 # Inputs to the model
query   = torch.randn(8, 64, 50)
key     = torch.randn(7, 32, 50)
value   = torch.randn(9, 16, 50)
__output__  = m(query, key, value)

