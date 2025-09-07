
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1):
       return torch.full([x1], 1)
 
# Initializing the model
m = Model()

 # Inputs to the model
x1  = (7,42)  # This tuple is used to initialize the model's input tensor. The first value of the tuple is the height and second is width. It should be between [50,68]. And it should be different from the previous one.
__output__=m(x1)