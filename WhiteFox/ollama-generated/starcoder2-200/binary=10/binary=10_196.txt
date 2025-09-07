
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(512, 768)
 
    def forward(self, x1):
        v1 = self.linear(x1) + torch.randn_like(v1) # Add a noise tensor to the output of the linear transformation
        return v1

# Initializing the model