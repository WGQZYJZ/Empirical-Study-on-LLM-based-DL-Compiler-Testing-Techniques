
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(64*64*3 ,1)
 
    def forward(self, x2):
        v0  =x2
        v1  =v0.view(-1, 64 * 64 * 3 ) # Transform the input tensor to a flat vector of size 64 * 64 * 3
        v2  =self.linear(v1)  # Apply the linear transformation with an output dimensionality equal to 1
        v3  =torch.sigmoid(v2) 
        return v3
 
# Initializing the model
m = Model()

