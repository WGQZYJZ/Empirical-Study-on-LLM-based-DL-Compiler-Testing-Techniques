
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(50, 3)
 
    def forward(self, x1):
        v1 = self.linear(x1)
        return v1


# Initializing the model and setting its hyper-parameters
m = Model()
__model_hyperparameters__ = {
    "lr": 0.05249786330395069, 
    "momentum": 0.3770080154638872, 
    "decay": 0.0
}


# Input to the model and its shape
x = torch.randn(30)
__input_shape__  = x.size()

# The hyper-parameters you are allowed to use during training should be included in this dictionary. 
# Hyperparameters which should not be tuned are removed by our script.
__allowed_hyperparameter_keys__  = ["lr", "momentum", "decay"]

