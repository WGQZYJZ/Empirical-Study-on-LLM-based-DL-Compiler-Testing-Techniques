
class Model(torch.nn.Module):
    def __init__(self, query, key):
        super().__init__()
        self.scale = torch.linalg.norm(query) / (torch.linalg.norm(key))
 
    def forward(self, x1):
        v1  = torch.matmul(x1, torch.transpose(self.scale, -2, -1)) # Compute the dot product of query and key using a custom scale factor.
        return v1


# Initializing the model
m = Model(torch.randn([8, 5]), torch.randn([7, 3]))

# Inputs to the model
x1  = torch.rand([2496])
