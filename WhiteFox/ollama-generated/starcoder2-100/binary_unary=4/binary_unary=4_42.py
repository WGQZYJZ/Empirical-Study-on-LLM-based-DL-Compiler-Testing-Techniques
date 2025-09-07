
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1=None): # Initializing the module to work in both training and evaluation modes by using the passed keyword argument (if exists) as another tensor that will be added with the input after the linear transformation
        v1  = torch.nn.Linear(3072,4*8)(x1) 
        v2  = v1 + torch.nn.Parameter(other) # Initializing the model to work in both training and evaluation modes by using the passed keyword argument (if exists) as another tensor that will be added with the input after the linear transformation
        v3  = nn.ReLU()(v2) 
        return v3
 
m  = Model()

