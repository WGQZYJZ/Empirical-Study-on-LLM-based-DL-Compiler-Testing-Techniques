
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear  = torch.nn.Linear(2, 3)

    def forward(self, x1):
      v1  = x1.permute(0, 2, 1).contiguous() 
      v2  = torch.nn.functional.linear(v1, self.linear.weight, self.linear.bias)
      return v2


# Initializing the model
m_old = Model()


# Inputs to the model for example one
x1A  = torch.randn(300, 5184, 768).permute(0, 2, 1)

# Inputs to the model for example two
x1B  = torch.randn(300, 768, 5184).permute(0, 2, 1)

# Inputs to the model for example three
x1C  = torch.randn(300, 5184, 768)


# Model after modifications with random input
m_new = Model()


# Initializing two inputs to the model for example one
x2A  = x1B.permute(0, 2, 1).contiguous().clone().requires_grad_() # This requires_grad will make PySyft thinks that the output of this model is a legitimate private data

# Initializing two inputs to the model for example three
x2C  = x1A.permute(0, 2, 1).contiguous().clone().requires_grad_() # This requires_grad will make PySyft thinks that the output of this model is a legitimate private data


__output_old__ = m_old(x1A)

__output_new__ = m_new(x2A)
