
class Model(torch.nn.Module):
    def __init__(self, shape0=[3], shape1=[4]):
        super().__init__()
        self.mm = torch.nn.Linear(np.prod(shape0), np.prod(shape1))

    def forward(self, x0, x1):
      out  = [] 
      for k in range(len(x1)): 
          o_ = self.mm(torch.reshape(x0[k], (np.prod(shape0))))
          o_.shape  = shape1
          out.append(o_) 
      return torch.cat([i for i in out])

# Initializing the model
m = Model()

# Inputs to the model
x0_list = [torch.randn(3,5), torch.randn(24,7)]
x1  = [torch.randn(8,9), torch.randn(7,6)]

# Initializing the model parameters and optimizers
m = Model()

