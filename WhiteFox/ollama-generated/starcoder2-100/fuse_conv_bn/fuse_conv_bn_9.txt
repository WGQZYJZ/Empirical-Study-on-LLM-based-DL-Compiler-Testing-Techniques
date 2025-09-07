
class Model(torch.nn.Module):
    def __init__(self,  dim1=2,  dim2=3) -> None:
        super().__init__()
        self.conv = torch.nn.ConvNd(dim1)
        self.bn = torch.nn.BatchNormNd(dim1)

    def forward(self, x):

        v_conv  =  self.conv(x) 
        v_output  =  self.bn(v_conv)
        return v_output

# Initializing the model
m = Model()

# Inputs to the model (2D/3D tensors with shape [batch, feature1, ..., featurn]) 
__input__  = torch.randn(10, dim1=4, dim2=dim3)

