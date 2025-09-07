
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1):
        v0  = torch.tensor([
            [
                [[23.,  78.],
                 [54.,   6.],
                 [90.,  -88.]],
 
                [[-29., 59],
                 [-87., 91.],
                 [35,  88.]]
            ]
        ])
        v1 = torch.nn.functional.conv2d(v0, self.weights) * 0.5 
        v2 = v1 * 0.7071067811865476 
        v3 = torch.erf(v2 )
        v4 = v3 + 1    
        v5 = v0[None, None] * v4
        return v5

# Initializing the model
m = Model()


# Inputs to the model
x1  = torch.randn(1, 8 ,64, 64)


# Input tensor
torch.manual_seed(3279090)
t = torch.nn.ConvTranspose2d(in_channels=5, out_channels=32, kernel_size=(1), stride=1, padding=None).to("cpu").weights()

