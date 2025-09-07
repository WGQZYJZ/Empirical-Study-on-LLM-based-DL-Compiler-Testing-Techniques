
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1):

        # Initialization
        v0 = torch.randn(32)

        # Computation block 1: linear transformation
        v1 = self.fc(v0)

        # Computation block 2: ReLU activation function (activation)
        v2 = self.activation(v1)
        
        return v2

# Initializing the model
m  = Model()
m.eval()

# Inputs to the model
x1  = torch.randn(32, 6400)

 # Generating output from model
__output__  = m(x1)

# Validation
import torch
import torch.nn as nn
from torchvision import models
from torchinfo import summary

 # Defining the model architecture (network structure) using PyTorch API. Note that the 'eval' function is used to ensure that all layers are in evaluation mode and do not have training-specific behavior. It is often useful to call this function during validation/testing when you want to ensure that your model behaves properly for inference.
class Model(nn.Module):
    def __init__(self):
        super().__init__()
        # Initialization
        self.fc = nn.Linear(6400, 128)

        # Activation layer (activation)
        self.activation = nn.ReLU()

    def forward(self, x1):

        # Initialization: a random vector of shape (32,) with values uniformly distributed between -1 and 1.
        v0 = torch.randn(32).cuda()


        # Computation block 1: linear transformation 
        v1 = self.fc(v0)

        # Computation block 2: ReLU activation function (activation)
        v2 = self.activation(v1)
        
        return v2

# Initializing the model
m = Model().cuda()
 
# Inputs to the model
x1  = torch.randn(32, 6400).cuda()

 # Generating output from model
output  = m(x1)

# Validating the accuracy of the model (Note that we are performing a forward pass through the model and computing its loss using standard PyTorch APIs.)
from torchmetrics import Accuracy

y_true = y.detach().cpu()

acc  = Accuracy()
acc_score  = acc(output, y)

