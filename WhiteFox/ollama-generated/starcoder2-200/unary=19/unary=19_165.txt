

class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(64*32*32, 1)

    def forward(self, x):
        t1 = self.linear(x).view(-1) 
        t2 = torch.sigmoid(t1) # Apply the sigmoid function to the output of the linear transformation
        return t2


# Initializing model
m  = Model()

# Inputs for model (input shape: [Batch size, Number of channels, Height of image, Width of image])
x  = torch.randn(100, 3, 64 , 64)
__output__  = m(x)

# Initializing the previous model
previous_model  = Model()
# Inputs for previous model (input shape: [Batch size, Number of channels, Height of image, Width of image])
previous_x1  = torch.randn(4000 , 32*64)

