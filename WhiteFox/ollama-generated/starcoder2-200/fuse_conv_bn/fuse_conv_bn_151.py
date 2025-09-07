
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 64, kernel_size=7)

    def forward(self, x1):
        v1 = torch.nn.functional.relu(x1)
        return torch.nn.functional.batch_norm(v1, training=False).detach()


# Initializing the model
m = Model()


# Inputs to the model 
x1 = torch.randn(256, 3, 480, 720) 


__output__  = m(x1) 

