
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1):

        # These 2 lines have been added to check whether the model has changed
        prev = m.__str__()
        curr = m().__str__()
        
        if not prev == curr:
            print('The model has changed')
        
        return torch.nn.functional.dropout(x1)

# Initializing the model
m  = Model()

 # Inputs to the model
 x1 = torch.randn(3,256,256)
 