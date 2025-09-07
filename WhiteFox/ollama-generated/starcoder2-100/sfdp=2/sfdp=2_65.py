
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, q1, k2, v3):
         return torch.matmul(q1, k2) + v3

 # Initializing the model
 m  = Model()

 # Inputs to the model