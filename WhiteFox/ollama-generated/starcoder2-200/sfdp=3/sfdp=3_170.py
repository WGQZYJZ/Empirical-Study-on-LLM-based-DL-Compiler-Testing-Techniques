
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.scale = 1 / (math.sqrt(64))
 
    def forward(self, q, k, v):
        o  = torch.matmul(q, k.transpose(-2, -1)) * self.scale
        o  = torch.nn.functional.dropout(torch.nn.functional.softmax(o), p=0.5)
        o  = torch.matmul(o, v)
        return o

# Initializing the model
m  = Model()

# Inputs to the model
key  = torch.randn((64, 32)) * math.sqrt(math.sqrt(32)) / (torch.rand(32).add_(0.1).rsqrt()).max_() # Initializing the key tensor in a manner that ensures that the dot product of query and keys is not zero
value = torch.randn((64, 32)) * math.sqrt(math.sqrt(32)) / (torch.rand(32).add_(0.1).rsqrt()).max_() # Initializing the value tensor in a manner that ensures that the dot product of query and keys is not zero
query = torch.randn((64, 32)) * math.sqrt(math.sqrt(32)) / (torch.rand(32).add_(0.1).rsqrt()).max_() # Initializing the query tensor in a manner that ensures that the dot product of query and keys is not zero

