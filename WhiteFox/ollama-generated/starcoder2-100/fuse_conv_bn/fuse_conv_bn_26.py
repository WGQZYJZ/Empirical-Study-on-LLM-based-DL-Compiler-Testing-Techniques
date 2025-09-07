
class Model(torch.nn.Module):
    def __init__(self, conv_fn = torch.nn.functional.conv2d):
        super().__init__()
        self.conv  = conv_fn
        self.bn  = torch.nn.BatchNormXd()
    
    def forward(self, x1): # x1 can be 1D or 3D
        if (x1.dim() == 1):
            input_shape = (1,) + tuple(x1.shape) + (-1,)
        else:
            assert(x1.dim()==2 or x1.dim() == 3), "The input must be a 1-D, or 2-D or 3-D tensor"
            input_shape = tuple(x1.shape)
            
        v1 = self.conv(torch.randn(*input_shape))
        return torch.nn.functional.batchnorm(v1, self.bn)

# Initializing the model
m = Model()

# Inputs to the model
x  = torch.randn([2] + [5]+ [-1]) # -1 is added to make sure the shape is dynamic
