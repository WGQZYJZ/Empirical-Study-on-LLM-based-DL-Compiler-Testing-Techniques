
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(32768, 10)
        self.relu = nn.ReLU()
 
    def forward(self, x):
        v1 = self.linear(x) # Apply a linear transformation to the input tensor
        v2 = self.relu(v1)# Apply ReLU on the output of the linear transformation
