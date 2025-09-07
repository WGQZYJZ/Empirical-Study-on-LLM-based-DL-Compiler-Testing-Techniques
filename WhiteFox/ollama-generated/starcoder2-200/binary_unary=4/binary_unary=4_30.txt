
class Model(torch.nn.Module):
    def __init__(self, *args, **kwargs):
        super().__init__()
        self.conv  = torch.nn.Linear(*args)
 
    def forward(self, x1):
        v0  = kwargs['other'] 
        v2  = v1 + v0
        v3  = F.relu(v2)
        return v3


# Initializing the model with some arguments for initialization of the linear transformation layer and a tensor to add as another input to the linear transformation
m  = Model(24, 8, bias=True)

