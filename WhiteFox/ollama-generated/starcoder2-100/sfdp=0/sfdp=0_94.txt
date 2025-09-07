
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, query, key, value):
        v1  = torch.matmul(query, key.transpose(-2, -1)) / np.sqrt(key.size()[-1]) 
        v3  = v1.softmax(dim=-1) 
        __output__  = v3 @ value
        return __output__

# Initializing the model
m  = Model().eval()

# Inputs to the model
query = torch.rand(8, 50)
key = torch.rand(8, 294, 50)
value = torch.rand(8, 137, 600)
