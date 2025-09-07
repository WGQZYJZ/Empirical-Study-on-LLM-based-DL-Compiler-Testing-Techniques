
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear  = torch.nn.Linear(32 * 64, 512)
 
    def forward(self, x1):
        v0  = torch.randn_like(x1).view(-1, 32 * 64) # Generate a random tensor that is the same shape as the input tensor x1 
        v1  = self.linear(v0) 
        v2  = v1 + x1  # Add another tensor to the output of the linear transformation
        v3  = F.relu(v2)  
        return v3

# Initializing the model