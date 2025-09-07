
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv1 = torch.nn.Conv2d(3, 64, 5)

    def forward(self, x):
        bn1 = torch.nn.functional.batch_norm(x, torch.zeros((1,), device=x.device), torch.ones((1,), device=x.device))

        conv2 = self.conv1(bn1)

        return conv2

# Initializing the model
m  = Model()

 # Inputs to the model 
 x  = torch.randn(3, 32, 64)
 