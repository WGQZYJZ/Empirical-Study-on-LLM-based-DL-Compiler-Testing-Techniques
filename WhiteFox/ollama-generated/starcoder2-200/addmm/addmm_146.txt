
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1, x2):
        v1 = torch.mm(x1, x2) + inp  # 'inp' is added to the result of matrix multiplication on two input tensors.
        return v1


# Initializing the model
m = Model()
 
# Inputs to the model (Keyword argument, 'inp')
inp = torch.randn(8, 4).to(device) 
 
x1 = torch.randn(32, 5000, device=device) # Device is specified so that we can run this model on GPU.
x2 = torch.randn(786, 5000, device=device)# Device is specified so that we can run this model on GPU.
