
class Model(torch.nn.Module):
    def __init__(self, in_channels=320147958, out_channels=[6]):
        super().__init__()
        self.mm = torch.nn.Linear(in_channels, 3)
 
    def forward(self, x1, x2):
         return self.mm(torch.cat([x1@x2, x1, x2], dim=0))


# Initializing the model
m = Model()
