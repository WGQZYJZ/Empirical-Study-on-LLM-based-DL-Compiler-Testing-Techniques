
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.scale  = math.sqrt(256)
 
    def forward(self, query, key, value):
         return torch.matmul(query, key.transpose(-2, -1)) / self.scale * 0.8


# Initializing the model
m  = Model()

# Input tensors for the model
query  = torch.randn(64, 32, 512)
key    = torch.randn(64, 32, 512)
value  = torch.randn(64, 32, 512)

 # Outputs from the model
 __output__  = m(query, key, value)
