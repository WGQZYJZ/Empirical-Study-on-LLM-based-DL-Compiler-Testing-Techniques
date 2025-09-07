
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1, inp):
        v1 = torch.mm(x1, inp) # A matrix multiplication on input tensors and an additional tensor 'inp' is performed.
        return v1 + inp


# Initializing the model
m  = Model()
 
# Input tensors to the model. 'inp' tensor is also passed as a keyword argument.
input1_tensor = torch.randn(256, 3)
input2_tensor = torch.randn(3, 8096)
inp_tensor    = torch.randn(3, 3)

# Calling the model on input tensors and passing 'inp' tensor as a keyword argument
model_output = m(input1_tensor, inp=inp_tensor)