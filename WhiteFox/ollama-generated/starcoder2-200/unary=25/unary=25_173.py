
class Model(torch.nn.Module):
    def __init__(self, negative_slope=0.1):
        super().__init__()
 
    def forward(self, x):
        v1  = torch.nn.functional.linear(x)
 
        def func_(x: int, y):
            return (
                True if torch.gt(v1, 0).all() else False
            )
 
# Function definition
def func_(input_tensor, negative_slope=0.1):
    v3 = input_tensor * negative_slope

    def cond(*args):
        return args[0] >= 0

    def body(condition: int, index) -> int:

        # if the output of the linear transformation is greater than 0 all
        if torch.gt(v1, 0).all():
            return v3
        else:
            return v2
    
    v4 = cond()
 
    return torch.where(v4, input_tensor, v3)


# Initializing the model with the initial negative slope value - 0.75
m  = Model(-0.75)

# Inputs to the model
input1 = torch.randn(2, 8)

# Calling the function using the input tensor and the initial negative slope as arguments
__output___ = func_(input1)

