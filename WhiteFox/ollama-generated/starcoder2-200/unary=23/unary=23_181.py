
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.convT  = torch.nn.ConvTranspose2d(3, 8, kernel_size=1)
 
    def forward(self, x1):
        v1  = self.convT(x1)
        v2  = torch.tanh(v1)
        return v2


# Initializing the model and generate input tensors
m = Model()
x1 = torch.randn(50, 3, 64, 64)
x2 = torch.zeros((50, 8, 79, 79)) # Generate a random tensor of shape [batch_size x output_channels x spatial_dim_H x spatial_dim_W] with all zeros


# Model evaluation (forward pass) - __output__ is the output obtained from m(x1) for the model with inputs `x1`
__output__  = m(x1, x2)

