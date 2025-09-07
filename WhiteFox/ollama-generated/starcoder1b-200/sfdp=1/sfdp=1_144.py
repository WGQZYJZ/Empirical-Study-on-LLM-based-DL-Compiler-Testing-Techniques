
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.query = torch.nn.Linear(1024, 2048)  # The query layer
        self.key   = torch.nn.Linear(1024, 2048)  # The key layer
        self.value = torch.nn.Linear(2048, 512)  # The value layer
 
    def forward(self, x):
        qk = torch.matmul(x, self.key.weight)  # Compute the dot product of the query and key tensors
        k  = qk / math.sqrt(self.key.weight.norm(2, dim=-1).pow(2).mean(-1))  # Scale the dot product by the inverse scale factor
        v  = torch.matmul(x, self.value.weight)
        output = torch.matmul(k, v)  # Compute the dot product of the key and value tensors
        return output


# Initializing the model
m = Model()

# Inputs to the model
x = torch.randn(1, 3, 64, 64)
