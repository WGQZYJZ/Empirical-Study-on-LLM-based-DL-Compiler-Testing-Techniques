
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def conv(self, x1):
        ...  # Define the main layer and its parameters and weight

        return  # The model is not updated, it is a simple way to define the network structure

    def batch_norm(self, x):
        ...  # Define the main layer and its parameters and weight
        return  # The model is not updated, it is a simple way to define the network structure

    def forward(self, x1):
        v1 = self.conv(x1)
        v2 = self.batch_norm(v1)

        return  # The model is not updated, it is a simple way to define the network structure


# Initializing the model
m = Model()


