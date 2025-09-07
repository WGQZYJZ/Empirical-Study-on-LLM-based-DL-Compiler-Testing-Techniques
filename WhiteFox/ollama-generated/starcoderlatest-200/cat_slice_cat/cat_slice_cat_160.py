
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, t1, t2, size, size_tensor):
        t3 = torch.cat([t1, t2], dim=1)
        return torch.cat([t3[:, 0:size], t3[:, 9223372036854775807-size:]], dim=1)

 # Initializing the model
m = Model()

 # Inputs to the model
x1 = torch.randn(1, 12, 64, 64)
x2 = torch.randn(1, 3, 128, 64)
