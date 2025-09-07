
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, ql, kl):
        v1 = torch.matmul(ql, kl) # Compute the dot product of query and key tensors
        return v1


# Initializing the model
m  = Model()


# Inputs to the model