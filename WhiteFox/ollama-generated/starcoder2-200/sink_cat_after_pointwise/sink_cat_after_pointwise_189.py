
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1):
      return torch.relu(x1)

 # Initializing the model
 m = Model()
 
 # Inputs to the model
 input  = torch.ones([32])
 
 # Expected output of the model on the inputs above