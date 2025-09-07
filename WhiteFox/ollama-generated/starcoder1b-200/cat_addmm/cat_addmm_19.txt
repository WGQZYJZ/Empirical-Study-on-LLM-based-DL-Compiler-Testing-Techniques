
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv1 = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
        self.fc1  = torch.nn.Linear(64*5*5, 64)
        self.fc2  = torch.nn.Linear(8,  64)
 
    def forward(self, x1):
        v1 = self.conv1(x1) # Apply pointwise convolution with kernel size 1 to the input tensor
        v2 = torch.cat([v1], dim=1)  # Concatenate a single element along an arbitrary dimension
        
        v3 = torch.matmul(v2, torch.tensor([[0.5]]).view(1, 64*5*5, 1))) # Calculate a constant
        v4 = torch.cat([torch.mul(v3, torch.tensor([0.7071067811865476])).view(1, 64*5*5, 1), v2], dim=1) # Perform matrix multiplication between v2 and a constant
        
        return v4


# Initializing the model
m = Model()


