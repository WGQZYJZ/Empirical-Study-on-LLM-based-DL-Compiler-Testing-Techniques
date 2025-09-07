
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

        self._conv  = torch.nn.Conv2d(3, 10, kernel_size=5)
        self._batchnorm  = torch.nn.BatchNorm2d(num_features=10)

    def forward(self, x):
         # the conv and batch norm is invoked in evaluation mode 
        return self._batchnorm(torch.nn.functional.conv2d(x, self._conv.weight))


# Initializing model
m  = Model()

# Inputs to the model
input_tensor  = torch.randn(10,3,5,7) # where the channel size is 3.
__output__  = m(input_tensor)

