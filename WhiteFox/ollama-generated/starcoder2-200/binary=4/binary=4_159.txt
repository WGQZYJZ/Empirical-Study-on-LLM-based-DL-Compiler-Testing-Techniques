
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(320 * 48, 512)
 
    def forward(self, x1):
        v1  = self.linear(x1)
        v2  = v1 + other_tensor # Add another tensor to the output of a layer
 
        return v2

# Initializing the model