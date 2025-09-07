
class Model(torch.nn.Module):
    def __init__(self, n_layers=1):
        super().__init__()
        self.cnn = torch.nn.Sequential(*[
            torch.nn.Conv2d(3, 40, kernel_size=(5,5)),
            torch.nn.ReLU(),
            torch.nn.Conv2d(40, 41, kernel_size=3),
            torch.nn.ReLU()
        ])
 
        if n_layers > 1:
            self.cnn_2 = torch.nn.Sequential(*[
                torch.nn.Conv2d(41, 40, kernel_size=(5,5)),
                torch.nn.ReLU(),
                torch.nn.Conv2d(40, 41, kernel_size=3),
                torch.nn.ReLU()
            ])
    
    def forward(self, x):
        out = self.cnn(x)
        return out + self.cnn_2(x)


# Initializing the model
m = Model()


