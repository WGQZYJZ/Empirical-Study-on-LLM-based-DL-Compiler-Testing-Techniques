
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.lin = torch.nn.Linear(2560, 384)
        self.relu1 = torch.nn.ReLU()
        self.dropout = torch.nn.Dropout(p=0.97)
 
    def forward(self, x1):
        v1  = self.lin(x1)
        v2  = v1 + other_tensor
        v3  = self.relu1(v2) 
        return v3


# Initializing the model
m = Model()
other_tensor = torch.randn(1, 50768).abs().int()

# Inputs to the model
x1  = torch.rand(1, 50768) # Generate a random tensor of shape (1, 50768)
