
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1):
        v2  = torch.cat([x1, self.linear], dim=0)
        v3  = v2.view(-1, 5, 8).sigmoid() 
        return v3


# Initializing the model
m  = Model()

# Input to the model for training
x1 = torch.randn(4, 5, 6)

# Input to the model for testing
x2 = torch.randn(7, 8)

# Inputs to the model for the purpose of printing out tensors in the forward function (to be used as arguments for the sink_cat_after_pointwise optimization)
x31, x32 = x2

# Training: Training the model by calling `m(x1)` and `m.forward()`
__output__  = m(x1)
__output__1  = m.forward()

# Testing: Testing the model by calling `m(x1)` on both `train=False` (i.e., testing phase) and train=True (i.e., training phase). The argument `train` is passed to the `train()` method.
__output2__  = m(x2, x31, x32, train=False)
__output3__  = m.forward()

