
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1):
        v1  = self.conv(x1)
        v2  = F.relu(v1)
        return v2

# Initializing the model
m = Model()

 # Inputs to the model
input_tensor = torch.randn(4096)
 
 # Initializing the criterion function 
 cost_fn  = nn.CrossEntropyLoss()
 
 # Loss and accuracy calculation
__outputs__, __labels__ = torch.max(__output__, dim=1, keepdim=True)
cost   = loss_fn(output_tensor, labels).item()


# Model