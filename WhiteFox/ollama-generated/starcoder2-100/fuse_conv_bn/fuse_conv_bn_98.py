
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1):  # x is not used by the model in this example.
        conv = torch.nn.ConvNd(2) 
        bn = torch.nn.BatchNormNd(2) 
        return bn(conv(x))


# Initializing the model
m  = Model()

# Inputs to the model
x1 = torch.randn(3, 480, 640) # 3 is for number of batches
__output__  = m(x1) 

