
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.mm = torch.nn.MM(bias=None)
 
    def forward(self, x1, inp: torch.Tensor):
        v1  = self.mm(x1, inp) 
        return v1


# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(640, 320) # A randomly generated tensor of shape (640 x 320). Please make sure this is different from your previous input tensors.
inp  = torch.zeros((592, 7)) # An empty 2-D Tensor with 592 rows and 7 columns.
__output__  = m(x1, inp)

