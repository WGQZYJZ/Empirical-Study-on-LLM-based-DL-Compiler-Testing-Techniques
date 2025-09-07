
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1):
      conv = torch.nn.Conv2d(x=3, y=6, kernel_size=(4, 5), stride=2) # The argument is fixed to 2 for testing purpose and could be modified by users later
      bn = torch.nn.BatchNorm2d(num_features=conv.weight.shape[1]) 
      conv = conv.to('cpu') 
      bn = bn.to('cpu')
      output = bn(conv(x1))
      return output


# Initializing the model 
m = Model()


# Inputs to the model 
x1 = torch.randn(2, 3, 500, 500) 
