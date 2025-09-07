
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv1 = torch.nn.Conv2d(3, 8, 5)

    def forward(self, x1):
        v1 = torch.nn.functional.batch_norm(x1) # batch normalization
        v2 = self.conv1(v1) 
        return v2
# Initializing the model
m  = Model()


# Inputs to the model
input  = torch.randn(1, 3, 80, 50).to("cuda")
