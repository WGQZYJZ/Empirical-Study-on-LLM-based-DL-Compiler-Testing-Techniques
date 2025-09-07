
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, arg1, arg2):
       t = torch.full([arg1, arg2], 1) # The first argument for this function is named "arg1" and the second one - "arg2".
       return t

# Initializing the model