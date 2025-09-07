
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.deconv = torch.nn.ConvTranspose2d(8, 3, 1)
 
    def forward(self, x1): 
        v1 = torch.nn.functional.relu(x1) # Applying the ReLU function to the input tensor
        return v1


# Initializing model