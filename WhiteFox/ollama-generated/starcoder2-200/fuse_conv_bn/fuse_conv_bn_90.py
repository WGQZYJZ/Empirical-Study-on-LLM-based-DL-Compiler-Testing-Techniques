
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1): 
        v3  = torch.nn.functional.convXd(x1, convXd_params, 1) # convolution layer
        v4  = torch.nn.functional.batchNormXd(v3, bn_params) # batch normalization layer
        return v4

# Initializing the model
m  = Model()

# Inputs to the model
x1  = torch.randn(16, 50, 28, 28), where X can be 1 or 3

