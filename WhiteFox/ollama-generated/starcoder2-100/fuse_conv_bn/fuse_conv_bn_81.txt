
class Model(torch.nn.Module):
    def __init__(self, convNd, batchNormNd):
        super().__init__()
        self.convNd = convNd
        self.batchNormNd = batchNormNd

    def forward(self, input1):
       output  = self.batchNormNd(self.convNd(input1)) 
       return output

# Initializing the model
m  = Model(torch.nn.Conv2d, torch.nn.BatchNorm2d)

 # Inputs to the model
x1 = torch.randn(10,3,32,32)
__output__|end_of_text__|end_of_text__|end_of_text__ = m(x1)

