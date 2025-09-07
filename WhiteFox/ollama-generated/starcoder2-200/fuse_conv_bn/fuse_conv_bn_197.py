
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, input):  # input should have shape [N x C]
        conv1 = torch.nn.Conv2d(32, 64, 7)
        bn1   = torch.nn.BatchNorm2d(64)

        return bn1(conv1(input))

# Initializing the model
m  = Model()

# Inputs to the model
input = torch.randn(8, 32, 50, 50).to("cuda")

 # __output__ is the output tensor. Please note that the final dimensions for this example will be [batch_size x num_channels]
__output__  = m(input)

# Constraints on the model
* ConvXd(N, C, X, K, P, S) 
* BatchNormXd(N, X) 

