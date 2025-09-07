
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, tensor1, tensor2):

        v  = torch.relu(tensor1)
        t3 = torch.cat([v, tensor2], dim=0).view(-1, 500)

        return t3

# Initializing the model
m = Model()

 # Inputs to the model