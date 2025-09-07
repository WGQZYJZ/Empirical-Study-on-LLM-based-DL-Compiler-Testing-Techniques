
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=0)
        self.linear = nn.Linear(64*64*8, 759705)
 
    def forward(self, x):
        v1 = self.conv(x) 
        v2 = F.relu(v1)
        v3 = torch.flatten(v2,start_dim=1) # Flattens a multi-dimensional tensor into one dimension with the size of 64 * 64 * 8
        v4 = self.linear(v3) 
        return v4

# Initializing the model
m  = Model()

 # Inputs to the model
x = torch.randn(1, 3, 64, 64)
 
 