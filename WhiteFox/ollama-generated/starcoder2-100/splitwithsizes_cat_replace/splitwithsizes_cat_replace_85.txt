
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1):
        x2  = torch.split(x1, 360, dim=0) # Here we assume the model only uses one split_tensor operation. We should also check that there is no concat operation in the model and the same dimension along which split and concatenate are performed.
        return torch.cat([x2[i] for i in range(len(x1))], dim=0)

# Initializing the model
m  = Model()
