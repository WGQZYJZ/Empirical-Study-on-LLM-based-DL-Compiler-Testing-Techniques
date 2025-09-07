
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, input1: Tensor, input2: Tensor, inp=None) -> Tensor:
        v1 = torch.mm(input1, input2) # Matrix multiplication on two inputs
        v2 = v1 + inp  # Add the result of the matrix multiplication to 'inp'
        return v2


# Initializing the model with arguments
model = Model()

# Inputs and arguments for the model
__output__, inp  = model(torch.randn(3,4), torch.randn(4,5)) # Output tensor and 'inp' argument
__output__
torch.Size([3, 5])

