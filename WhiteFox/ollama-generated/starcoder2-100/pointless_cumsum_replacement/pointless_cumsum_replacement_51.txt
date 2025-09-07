
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x):
         return torch.cumsum(convert_element_type(x1, x2), 0)

 # Initializing the model