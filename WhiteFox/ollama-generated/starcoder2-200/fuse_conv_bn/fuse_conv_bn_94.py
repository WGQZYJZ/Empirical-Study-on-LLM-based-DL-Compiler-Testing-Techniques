
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1):
        conv = torch.nn.ConvXd(2048)
        bn  = torch.nn.BatchNormXd()

        return conv(x1).permute([0, 3, 1, 2])


# Initializing the model
m  = Model() 

# Inputs to the model
x1 = torch.randn(5, 2048)  # Input tensor to the model with 5 data points and 2048 features each
