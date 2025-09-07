
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear  = torch.nn.Linear(25088, 64)
 
    def forward(self, x1):
        v1  = self.linear(x1)
        v2  = F.relu(v1)
        return v2


# Initializing the model:
m  = Model()
 
# Input tensor to the model:
x1  = torch.randn(64, 50 * 50 * 3) # (number of samples x number of pixels in an image)
 
# Running the model on the input data
