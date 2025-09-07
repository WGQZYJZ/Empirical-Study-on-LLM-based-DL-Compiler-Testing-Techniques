
class Model(torch.nn.Module):
    def __init__(self, num_layers=10):
        super().__init__()
 
        self.convs = torch.nn.ModuleList([
            torch.nn.Conv2d(3, 8, 1, stride=1, padding=1),
        ])
        for i in range(num_layers - 1):
            self.convs.append(
                torch.nn.Sequential(
                    torch.nn.ReLU(),
                    torch.nn.MaxPool2d(2)))
 
        self.fc = torch.nn.Linear(8 * (num_layers - 2), 4)
 
    def forward(self, x):
        convs = [conv(x) for conv in self.convs]
        flat_convs = torch.cat(convs, dim=1)
 
        fc = self.fc(flat_convs)
        return fc


# Initializing the model
m  = Model()


# Inputs to the model
x = torch.randn(1, 3, 64, 64)
