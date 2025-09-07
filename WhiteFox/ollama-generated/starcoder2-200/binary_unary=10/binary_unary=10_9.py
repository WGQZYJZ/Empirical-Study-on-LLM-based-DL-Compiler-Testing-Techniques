
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1):
        v = torch.nn.Linear()(x1) # Apply linear transformation to an input tensor
        v += 5 # Add another constant value to the result of the linear transformation
        v = self._relu(v) # Apply ReLU function to the result of the linear transformation plus a constant value (the new tensor is not equal to the previous one in value but it should be treated as such). The function of ReLU is `_relu` that you can find here: https://pytorch.org/docs/stable/_modules/torch/nn/functional.html#relu
        return v


# Initializing the model 
m = Model()

# Inputs to the model
x1 = torch.randn(5, 3) # A tensor that is different from the previous one in both shape and value. 
 __output__  = m(x1)
 
