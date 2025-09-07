
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1, inp):
        v1 = torch.mm(x1, inp)
        return 0 + v1
 
 
 # Initializing the model
 m  = Model()

 # Inputs to the model
 inp = torch.randn(524288).reshape(1024, 523976)
 x1 = torch.randn(1024, 523976)
 