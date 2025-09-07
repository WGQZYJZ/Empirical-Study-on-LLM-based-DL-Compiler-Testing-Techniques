
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv1 = torch.nn.Conv2d(3, 8, 3, stride=1, padding=0)
        self.maxpool = torch.nn.MaxPool2d(2, stride=2)
 
    def forward(self, x):

        split_tensors = torch.split(x, [4], dim=0)
        concatenated_tensor = torch.cat([split_tensors[i] for i in range(len(split_tensors))], 1)
        return concatenated_tensor

# Initializing the model
m  = Model()

 # Inputs to the model
x  = torch.randn(4, 3, 65, 67)
