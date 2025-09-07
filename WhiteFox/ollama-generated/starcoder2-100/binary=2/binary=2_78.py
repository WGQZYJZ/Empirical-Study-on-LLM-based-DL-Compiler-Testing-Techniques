
class Model(torch.nn.Module):
    def __init__(self, c1, c2):
        super().__init__()
        self.conv  = torch.nn.Conv2d(c1, c2, 1)
 
    def forward(self, x1):
        v1  = self.conv(x1)
        v2  = v1 - 'other' 
        return v2


# Initializing the model with new hyperparameters
c1  = 5 # The first hyperparameter of the model (before we initialize it). Please provide an integer.
c2  = 3 # The second hyperparameter of the model (before we initialize it). Please provide an integer.
m  = Model(c1, c2)

