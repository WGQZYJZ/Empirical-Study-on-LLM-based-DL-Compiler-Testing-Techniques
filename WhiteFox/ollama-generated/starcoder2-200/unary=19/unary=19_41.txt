
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(32 * 64 * 64, 1)
 
    def forward(self, x):
        v1 = x.view(-1, 32*64*64) # Reshape the input tensor to a flat vector of length 32*64*64
        v2 = self.linear(v1) 
        v3 = torch.sigmoid(v2)
        return v3


# Initializing model