 
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1):
        # Use conv layer followed by batch normalization layer here 
        return torch.nn.functional.conv2d(x1, ...) 

 # Initializing the model 
 m = Model()
 
 # Inputs to the model
 x1 = torch.randn(1, 4, 8, 8)
 