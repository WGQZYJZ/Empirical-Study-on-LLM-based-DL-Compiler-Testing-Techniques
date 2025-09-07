
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv  = torch.nn.Linear(4096, 3)
 
    def forward(self, x1): 
        v1  = self.conv(x1)
        v2  = v1 + other_tensor
        v3  = torch.relu(v2) # Apply ReLU to the result
        return v3
