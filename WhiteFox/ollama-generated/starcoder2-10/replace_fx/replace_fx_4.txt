
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.dropout  = torch.nn.Dropout2d(0.5, inplace=True)

    def forward(self, x1):
        v1  = torch.nn.functional.dropout(x1, self.dropout.p, True)
        v2  = torch.rand_like(v1, None, device="cpu", dtype=v1.dtype, layout=v1.layout, requires_grad=v1.requires_grad) 
        return v2


# Initializing the model
m  = Model()


# Inputs to the model
x1 = torch.rand(20)

 # Running the model for some time and generating the trace of the backward pass
__output__, x1 = m(x1)

import torch
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1):
        v3  = torch.sum(x1) 
        return v2


# Initializing the model
m  = Model()

# Inputs to the model
x1  = torch.rand(500)

# Running the model for some time and generating the trace of the backward pass
__output__, x1, v3 = m(x1)

 # 