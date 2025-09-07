
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(512, 768)
 
    def forward(self, query, key, value):
        v1 = torch.matmul(query, key.transpose(-2, -1)) # Compute the dot product of a query and a key
        v3 = v1 * 0.9
        v4 = self.linear(v3) 
        return v4


# Initializing the model
m = Model()

# Input tensors to the model
query = torch.randn(2, 64, 512)
key = query.transpose(-2, -1).clone().detach()
value = key * 0.9

# Output tensor from the model
